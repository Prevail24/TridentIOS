# Trident Knowledge Base
# Machine-003
# Paperwork (Hack The Box)

Difficulty: Easy
Platform: Hack The Box
Season: 11
Completion Date: July 19, 2026

Status:
ROOTED

---

# Objective

Use TridentIOS and Medusa against the Hack The Box machine Paperwork,
observe where the current investigation platform succeeds,
and identify where manual operator action is still required.

This was the first live HTB run after Recon gained three weapons:

- Nmap
- HTTPX
- Gobuster

---

# Mission Artifacts

Mission:

MIS-2026-0013

Target:

10.129.59.213

Nmap Run:

RUN-2026-0066

HTTPX Run:

RUN-2026-0067

Downloaded Evidence:

knowledge/evidence/http/paperwork-archive-v1.02.zip

Archive SHA256:

d66fd470fb2d9a719f56dc089611dae716739fbe19bf107daa53c1cad397127c

---

# Attack Chain

Internet

|

v

Nginx on port 80

|

v

Redirect to paperwork.htb

|

v

Document Archiving Service

|

v

Download paperwork-archive-v1.02.zip

|

v

Review server.py

|

v

Discover LPD service on port 1515

|

v

Command injection in LPD print job name

|

v

Shell as lp

|

v

Local JetDirect service on 127.0.0.1:9100

|

v

PJL filesystem traversal

|

v

Read user.txt as archivist

|

v

Write archivist authorized_keys

|

v

SSH as archivist

|

v

paperwork-daemon file descriptor leak

|

v

Recover ADMIN_PASSWORD

|

v

su to root

---

# Initial Recon

Medusa created and activated the mission.

Nmap identified:

- 22/tcp ssh OpenSSH 10.0p2 Ubuntu 5ubuntu5.4
- 80/tcp http nginx 1.28.0 Ubuntu

This confirmed Trident's first live HTB behavior:

Nmap successfully collected canonical observations and attached them to the active mission.

---

# First Trident Lesson

The web service redirected IP-based traffic:

http://10.129.59.213/

to:

http://paperwork.htb/

That exposed an immediate platform gap.

HTTPX and Gobuster can execute,
but the current weapons do not yet understand mission vhosts,
Host headers,
or operator-provided DNS mappings.

Result:

HTTPX produced an empty run until the vhost was handled manually.

Required future work:

- Detect HTTP redirects to hostnames.
- Add discovered vhosts to MissionContext.
- Let HTTPX and Gobuster run with Host headers.
- Teach the Planner to pause content discovery until vhost resolution is handled.

---

# Web Application

After resolving the vhost manually,
the landing page identified itself as:

Intranet | Document Archiving Service

Important page clues:

- Maintenance advisory for backend spooler PRN-ARCHIVE-01.
- Compliance level RFC 1179.
- Target queue archive_intake.
- Download link for paperwork-archive-v1.02.

The archive endpoint:

/download/archive

returned:

paperwork-archive-v1.02.zip

The archive contained:

server.py

---

# LPD Source Review

The downloaded source described a custom LPD server.

Important details:

- The queue name came from LPD_QUEUE.
- The expected queue was archive_intake.
- The service listened on port 1515.
- A print job control file field beginning with J was treated as the job name.
- The job name was passed into a shell command.

The live target version confirmed the issue:

subprocess.Popen(..., shell=True)

The attacker-controlled print job name reached the shell.

---

# Targeted Port Discovery

The first default Nmap run found ports 22 and 80 only.

After source review,
a targeted scan checked port 1515.

Result:

1515/tcp open

Service response:

Archive_Printer is ready and printing.

This was the second platform lesson.

Trident needs a targeted service discovery mode.

The initial Nmap weapon did its job,
but the investigation produced a new hypothesis:

"The web clue mentions a backend spooler. Check the spooler port."

That is Planner behavior.

---

# Initial Access

A benign callback proof was sent through the LPD queue.

The callback landed from:

10.129.59.213

This confirmed code execution as the LPD service user.

A controlled reverse shell then produced:

uid=7(lp) gid=7(lp) groups=7(lp)

Working directory:

/opt/LPDServer

Initial access user:

lp

---

# Local Enumeration

Interesting local users:

- lp
- archivist

Interesting processes:

- /usr/bin/python3 /opt/LPDServer/server.py
- /usr/bin/python3 /home/archivist/printer/jetdirect.py 9100 /home/archivist/printer/ /home/archivist/printer/logs/commands.log
- /usr/bin/python3 /usr/bin/paperwork-daemon
- /usr/bin/python3 /root/staging/CorpoSite/app.py

Interesting local sockets:

- 127.0.0.1:9100 JetDirect-like printer service
- /run/paperwork/mgmt.sock

The management socket permissions were:

root:archivist 660

This suggested the intended pivot:

lp -> JetDirect -> archivist -> management socket -> root material

---

# JetDirect Pivot

The local JetDirect service responded to PJL:

HP LASERJET 4ML

The PJL filesystem exposed:

- logs/
- jetdirect.py

PJL FSUPLOAD recovered the JetDirect source.

Critical issue:

The service translated printer paths into filesystem paths,
but did not enforce that the final normalized path stayed inside its root.

The root directory was:

/home/archivist/printer

Traversal allowed reading:

0:\\..\\user.txt

which resolved to:

/home/archivist/user.txt

User flag:

e50ac454d878ca6018e61939a80a6793

---

# Stabilizing as archivist

The same PJL file primitive could write files as archivist.

authorized_keys existed but was empty:

/home/archivist/.ssh/authorized_keys

A temporary SSH public key was written through PJL.

SSH confirmed:

uid=1000(archivist) gid=1000(archivist) groups=1000(archivist)

The temporary key was removed during cleanup.

---

# Root Path

The root-owned daemon:

/usr/bin/paperwork-daemon

opened:

/etc/paperwork/admin_pins.conf

It also watched:

/home/archivist/printer/logs/commands.log

If the log contained any of:

- FSQUERY
- FSUPLOAD
- FSDOWNLOAD

then the daemon sent file descriptors over:

/run/paperwork/mgmt.sock

The socket was readable by the archivist group.

Connecting to the socket as archivist returned:

ALERT: SECURITY_VIOLATION. FORENSIC_CONTEXT_ATTACHED.

The attached file descriptors included:

- commands.log
- admin_pins.conf

Recovered secret:

ADMIN_PASSWORD=ApparelMortuaryCedar22

That password worked with:

su -

Root confirmed:

uid=0(root) gid=0(root) groups=0(root)

Root flag:

8dda668ae7e062990d51264244129ef4

---

# Cleanup

Performed cleanup:

- Removed the temporary SSH key from archivist authorized_keys.
- Removed the temporary local SSH keypair.
- Closed the root SSH session.
- Closed the lp reverse shell.
- Stopped the callback listener.

Remaining local Trident artifacts are mission evidence,
observations,
relationships,
tool runs,
and the downloaded archive.

---

# What Trident Did Well

Trident successfully:

- Created and activated a mission.
- Ran Nmap through Medusa.
- Stored canonical Nmap observations.
- Preserved evidence for the Nmap run.
- Created mission artifacts for later review.
- Helped expose where the architecture needs the next capabilities.

The platform behaved like an investigation notebook with sensors attached.

That is real progress.

---

# Where the Operator Took Over

Manual work was required for:

- Handling the paperwork.htb vhost.
- Re-running HTTPX with the correct Host context.
- Downloading and inspecting the archive.
- Inferring that port 1515 mattered.
- Sending an LPD protocol proof.
- Pivoting through PJL on localhost 9100.
- Reading file descriptors from the management socket.

This was not a failure.

This was the point of the live run.

The box showed exactly where Trident must grow next.

---

# Engineering Lessons

## Vhost Intelligence

When HTTP redirects to a hostname,
Trident should record that hostname as a discovered web identity.

MissionContext needs to represent:

- target IP
- discovered hostname
- scheme
- port
- required Host header

HTTPX and Gobuster should consume that context.

---

## Targeted Service Discovery

The default Nmap pass was not enough.

The downloaded source mentioned port 1515.

The future Planner should convert source evidence into a targeted scan:

If artifact mentions a port,
then run targeted service discovery against that port.

---

## Artifact Ingestion

The downloaded zip was decisive.

Trident needs an artifact ingestion capability:

- Download file.
- Hash it.
- Store it as evidence.
- Identify file type.
- List archive contents.
- Extract source safely.
- Produce observations from static review.

---

## Manual Breakthrough Observations

Some discoveries came from operator reasoning,
not from a current weapon.

Trident needs a first-class way to record:

- hypothesis
- manual command
- observed result
- conclusion

This should still flow through MissionContext,
Sensors,
and the Observation Engine.

---

## Future Capabilities Suggested

This machine suggests new capabilities:

- Vhost Discovery
- Artifact Retrieval
- Archive Inspection
- Source Review
- Targeted Port Scan
- Local Service Enumeration
- Printer/PJL Assessment
- Unix Socket Assessment

Not all of these need to be automatic immediately.

But Trident should know how to represent them.

---

# Significance

Paperwork was the first live HTB machine completed after Recon gained:

- Service Discovery
- Technology Discovery
- Content Discovery

It proved that the current architecture can support a real investigation.

It also proved that the next big architectural need is not another standalone tool.

The next need is planning.

Not AI planning.

Deterministic,
evidence-driven,
mission-aware planning.

Paperwork became the first live proof that Trident can observe,
that the Observer can reason,
and that the system can now tell us what it needs to become next.
