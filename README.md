# NomaanOS-ShieldSOC

Edge telemetry adapter for the NomaanOS security ecosystem.

## Current status

This repository currently provides a small, dependency-free telemetry adapter. It deliberately returns `None` for CPU temperature when no sensor reader is injected and reports integrity as `UNVERIFIED` unless a verifier is explicitly supplied. It must not be presented as a complete SOC or as proof that a host is secure.

## Extension points

- Inject a platform-specific CPU temperature reader.
- Inject an integrity verifier backed by measured file or boot state.
- Send structured events to NomaanOS-EvidenceLedger.
- Add alert rules, persistence, authentication, and access control before deployment.

## Run

```bash
python shield_monitor.py

Security
​See SECURITY.md. Telemetry is observational and should be treated as untrusted input.
