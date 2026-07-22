# Trident Knowledge Base
# Machine-004
# Bedside (Hack The Box)

Difficulty: Medium
Platform: Hack The Box
Season: 11
Date Started: July 19, 2026

Status:
IN PROGRESS

---

# Objective

Use TridentIOS and Medusa against the Hack The Box machine Bedside,
capture the investigation trail,
identify where Trident succeeds,
and preserve the remaining open leads for continued work.

This run exercised the current Recon stack:

- Nmap
- HTTPX
- Gobuster
- HTTP artifact retrieval

It also exposed the need for a new Recon capability:

- Virtual host discovery

---

# Mission Artifacts

Primary target:

10.129.36.93

Observed hostnames:

- bedside.htb
- research.bedside.htb

Active mission observed during the run:

MIS-2026-0023

Important runs:

- RUN-2026-0079 — Nmap
- RUN-2026-0080 — HTTPX
- RUN-2026-0081 — Gobuster against bedside.htb
- RUN-2026-0082 — HTTP artifact retrieval for bedside.htb index.php
- RUN-2026-0089 — HTTP artifact retrieval for research.bedside.htb index.php
- RUN-2026-0091 — Gobuster against research.bedside.htb

Important evidence:

- knowledge/evidence/http/RUN-2026-0082-index.php
- knowledge/evidence/http/RUN-2026-0089-index.php

Research portal evidence SHA256:

09bb23f49150b53e5e62cdfad4ff67071dd3dfbaac4aceffcefd1968b89f3cd5

---

# Initial Connectivity Issue

The first scans failed because macOS routed the target through the wrong interface.

The Release Arena VPN interface was:

utun13

with local VPN address:

10.10.15.5

The target initially routed through the normal network interface instead of the VPN.
After adding a host route through the Release Arena VPN,
Nmap began receiving responses normally.

Lesson:

Trident should eventually include a preflight route check for HTB targets.

---

# Initial Recon

Nmap identified:

- 22/tcp ssh OpenSSH 10.0p2 Debian 7+deb13u4
- 80/tcp http Apache httpd 2.4.68
- 3000/tcp filtered

HTTPX identified the IP-based web response:

http://10.129.36.93

which redirected to:

http://bedside.htb/

HTTPX recorded:

- Status: 301
- Redirect: http://bedside.htb/
- Web server: Apache/2.4.68 Debian
- Technologies: Apache HTTP Server 2.4.68, Debian

---

# Main Web Surface

Hostname:

bedside.htb

The page presented a simple Bedside Clinic landing page.

Visible content:

- Bedside Clinic
- AI heart care theme
- About Us
- Treatments
- AI Innovations
- Contact
- Schedule a Consultation button

Important contact clue:

contact@bedside.htb

The Schedule a Consultation button was only an in-page anchor:

```html
<a href="#contact" class="btn">Schedule a Consultation</a>
```

Direct route checks:

- /contact returned 404
- /schedule returned 404

Conclusion:

The button itself does not call a backend route.
The landing page is likely thematic direction toward AI, research, and file processing.

---

# Gobuster Against bedside.htb

Initial Trident Gobuster found:

- /index.php — 200
- /javascript/ — 301
- /server-status — 403
- Apache dotfile noise — 403

No useful application routes were exposed on the main vhost.

---

# Virtual Host Discovery

The first vhost scan was noisy because unknown hostnames produced 301 redirects back to:

http://bedside.htb/

Filtering out status 301 revealed the meaningful host:

research.bedside.htb

Observed response:

- Status: 200
- Size: 3152

This was the main pivot point of the investigation.

Useful command shape:

```bash
gobuster vhost \
  -u http://10.129.36.93 \
  -w libraries/wordlists/web-content/raft-small-words.txt \
  --append-domain \
  --domain bedside.htb \
  -t 30 \
  --exclude-status 301
```

---

# Research Portal

Hostname:

research.bedside.htb

Title:

Bedside Research Portal

Purpose described by page:

The portal allows staff to upload X-rays,
fluoroscopy images,
CT scans,
and research documents for AI model training.

Upload form:

```html
<form method="post" enctype="multipart/form-data">
<input type="file" name="uploadFile" required>
```

Visible accepted formats:

- jpeg
- jpg
- png
- bmp
- tiff
- dcm
- pdf

The page also states:

Collections can be uploaded as archives.

Response header:

```text
X-Powered-By: pdfminer.six
```

This is a high-value clue.

---

# Upload Behavior

Benign upload tests confirmed that uploaded files are stored under:

```text
/var/www/research.bedside.htb/uploads
```

The application leaked this path during a validation failure:

```text
MIME type mismatch. Unable to upload file to destination /var/www/research.bedside.htb/uploads
```

Files are retrievable at:

```text
http://research.bedside.htb/uploads/<filename>
```

The uploads directory itself is forbidden:

```text
/uploads/ -> 403
```

but individual known filenames are served directly.

---

# Accepted and Rejected File Types

Accepted during safe testing:

- png
- zip
- pdf
- dcm
- gz

Rejected during safe testing:

- php
- phtml
- phar
- txt
- png.php
- fake PDF with mismatched content

The full allowed extension list leaked by the application:

```text
jpeg, jpg, png, bmp, tiff, dcm, pdf, gz, zip
```

Filename handling:

- Traversal-style filenames were sanitized.
- Spaces were normalized to underscores.
- Double extension ending in a disallowed extension was rejected.

Observed examples:

- ../solprobe_traverse.png became solprobe_traverse.png
- solprobe space.png became solprobe_space.png
- solprobe_double.png.php was rejected

---

# Storage and Processing Observations

PNG files:

- accepted
- retrievable directly

ZIP files:

- accepted
- stored as ZIP
- not extracted into /uploads

PDF files:

- accepted
- stored unchanged
- served as static application/pdf
- no obvious text, JSON, or image sidecar was created

DICOM files:

- accepted
- stored unchanged
- served as application/dicom
- no obvious PNG, JPG, or text sidecar was created

This suggests uploads are stored immediately,
but no visible processing happens at upload time.

---

# pdfminer.six Advisory Lead

The `X-Powered-By: pdfminer.six` header,
combined with accepted PDF and GZ uploads,
matches the shape of the pdfminer.six advisory:

GHSA-wf5f-4jwr-ppcp

Reference:

https://github.com/pdfminer/pdfminer.six/security/advisories/GHSA-wf5f-4jwr-ppcp

The relevant condition:

A PDF must be processed by pdfminer.six.

The investigation safely tested the placement pieces:

- A `.pickle.gz` file can be uploaded.
- A PDF can reference the expected upload path.
- The upload path is known.

Safe marker and callback probes did not trigger on the target.

Important conclusion:

The files can be placed,
but the processing trigger has not been found.

The current state is:

```text
Uploaded: yes
Stored: yes
Triggered by server-side processing: not confirmed
```

Possible explanations:

- The portal stores uploads but does not immediately process them.
- A scheduled worker processes files later.
- A staff/admin workflow triggers processing.
- A hidden route previews or extracts uploaded PDFs.
- pdfminer.six is present but not used for submitted files.
- The installed version or environment may be constrained.

Do not mark this lead as confirmed exploitation.
It is an active hypothesis.

---

# Trigger Path Hunting

Focused endpoint discovery on research.bedside.htb looked for:

- analyze
- api
- convert
- download
- extract
- file
- ingest
- job
- parse
- pdf
- preview
- process
- result
- scan
- status
- text
- train
- upload
- viewer

Only known paths were found:

- /
- /index.php
- /uploads/

Query parameter checks against index.php returned the normal upload page.

Examples:

- ?file=uploads/<pdf>
- ?pdf=uploads/<pdf>
- ?view=<pdf>

Fetching uploaded PDFs directly only caused Apache to serve the PDF statically.
It did not appear to invoke pdfminer server-side.

---

# Contact and Email Lead

The main page exposed:

contact@bedside.htb

This may be a username or story clue,
but no exposed mail service was found.

Mail ports checked:

- 25 closed
- 110 closed
- 143 closed
- 465 closed
- 587 closed
- 993 closed
- 995 closed

Direct vhost checks:

- contact.bedside.htb redirected to bedside.htb
- mail.bedside.htb redirected to bedside.htb

Focused schedule/contact terms did not reveal additional paths or vhosts.

Current interpretation:

The email is likely contextual or a potential username clue,
not a directly exposed mail-service path.

---

# Current Attack Surface Summary

Confirmed:

- SSH is open on port 22.
- Apache is open on port 80.
- Main vhost is mostly static.
- research.bedside.htb is the main application surface.
- The research portal allows controlled file uploads.
- Uploaded files are directly retrievable by known filename.
- The portal leaks pdfminer.six.
- The portal leaks the server upload path.

Unconfirmed:

- Whether uploaded PDFs are processed automatically.
- Whether a hidden processing endpoint exists.
- Whether a background worker processes uploads later.
- Whether port 3000 becomes reachable from another context.
- Whether contact@bedside.htb is useful as a credential clue.

---

# Trident Lessons

This box produced several concrete platform improvements.

Needed:

- Vhost Discovery Capability
- Gobuster vhost mode
- Gobuster extension support
- Host-header support from Observer commands
- Upload Surface Observation type
- Header capture in Mission Intelligence
- Route/VPN preflight check
- Long-running tool progress streaming
- Ctrl-C handling that returns to Observer instead of killing Medusa
- Case/Mission association tightening

This investigation also showed that Trident should distinguish:

```text
file uploaded
file stored
file retrievable
file processed
```

Those are different observations.

Implemented after this investigation:

- Added Gobuster vhost mode to the Gobuster pipeline.
- Added canonical `web_vhost` observations.
- Added Virtual Host Discovery capability.
- Added Gobuster extension support.
- Exposed Host-header and extension options in Observer Gobuster.
- Added Observer `vhost` command.
- Added Observer `vhosts` view.

New Observer command examples:

```text
vhost http://10.129.36.93 bedside.htb libraries/wordlists/web-content/raft-small-words.txt --exclude-status 301
```

```text
gobuster http://10.129.36.93 libraries/wordlists/web-content/common.txt --host research.bedside.htb --extensions php,bak,old,conf,env,zip,gz,phps
```

---

# Next Steps

Continue looking for the processing trigger.

Most valuable next investigations:

- Search for a hidden preview or processing workflow.
- Revisit uploaded files after time has passed in case a worker runs periodically.
- Watch for any new files or transformed artifacts by known filename.
- Continue vhost discovery with smaller thematic lists.
- Treat contact@bedside.htb as a possible username only if a login surface appears.
- Keep port 3000 in mind as filtered, but do not force it without a reason.

Current operator read:

The intended path likely involves the research upload workflow,
but the processing event has not yet been discovered.
