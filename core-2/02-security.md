# Core 2 · Domain 2 — Security (28%)

## Physical security
Bollards, access control vestibule (mantrap), badge readers, video surveillance, alarm systems, motion sensors, door locks, equipment locks, guards, fences, biometrics (fingerprint, retina, facial), key fobs, smart cards.

## Logical security
- **Principle of least privilege**, zero trust.
- **MFA** factors: something you know / have / are / somewhere you are.
- Email, hard token, soft token (authenticator app), SMS, voice call.
- ACLs, SSO, **Active Directory**: domain, OU, group policy, login scripts, home folders, folder redirection.
- **AAA**: Authentication, Authorization, Accounting.

## Wireless security
- **WPA3** (best, SAE) > WPA2 (AES/CCMP) > WPA/TKIP (avoid) > WEP (never).
- Personal (pre-shared key) vs Enterprise (RADIUS/TACACS+/Kerberos).
- Change default SSID/password, disable WPS, firmware updates.

## Malware types
| Type | What it does |
|---|---|
| Virus | Attaches to files, needs user action |
| Worm | Self-replicates across network |
| Trojan | Disguised as legit software |
| Ransomware | Encrypts files, demands payment |
| Rootkit | Hides deep in OS (needs boot-time scan / reimage) |
| Keylogger | Records keystrokes |
| Spyware | Monitors user |
| Botnet | Remote-controlled zombie machines |
| Cryptominer | Uses your CPU/GPU to mine |
| Stalkerware, fileless malware, PUPs | — |

Tools: antivirus/anti-malware, recovery console, Windows Defender, EDR/MDR/XDR, email security gateway, user education, OS reinstall.

## Social engineering & threats
Phishing, vishing (voice), smishing (SMS), whaling (executives), spear phishing, shoulder surfing, tailgating, piggybacking, impersonation, dumpster diving, evil twin, DoS/DDoS, zero-day, spoofing, on-path (MITM), brute force, dictionary, insider threat, SQL injection, XSS, BEC (business email compromise), supply chain attack, non-compliant systems, unpatched systems, EOL OS.

## Windows security settings
- Defender Antivirus & Firewall, users & groups (Administrator, Standard, Guest, Power Users).
- **NTFS vs share permissions**: most restrictive wins when combined; explicit deny beats allow; inherited permissions; moving within same volume keeps permissions, copying inherits destination.
- UAC, BitLocker / BitLocker To Go, EFS (file-level encryption, NTFS only).
- Run as administrator, Windows Hello, passwordless, Microsoft account vs local account.

## Workstation hardening
Strong passwords, lock screen timeout, BIOS/UEFI passwords, disable AutoRun, disable guest account, change default admin passwords, failed-login lockout, end-user education.

## Mobile security
Screen locks (PIN, biometrics, pattern), remote wipe, locator apps, OS updates, device encryption, MDM, BYOD vs corporate-owned, profile security.

## Data destruction
- Physical: shredding, drilling, degaussing (HDD only), incineration.
- Recycling/repurposing: erasing/wiping, low-level format, standard format (not secure).
- Outsourcing → get a **certificate of destruction**.

## SOHO router security
Change default credentials, firmware updates, content filtering, IP filtering, port forwarding vs port triggering, disable UPnP, DMZ, screened subnet, static IPs, disable SSID broadcast (weak), guest network.

## Browser security
Trusted sources, hashing downloads, extensions/plug-ins, password managers, secure connections (HTTPS/certificates), pop-up blockers, clearing cache, private browsing, sync.

## My notes
