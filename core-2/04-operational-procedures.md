# Core 2 · Domain 4 — Operational Procedures (21%)

## Documentation & support systems
Ticketing system (user info, device info, description, categories, severity, escalation levels, clear problem/resolution notes), asset management (inventory, database, procurement lifecycle, warranty, assigned users), knowledge base, SOPs, AUP, incident reports, new-user/offboarding checklists, regulatory compliance, splash screens.

## Change management
Documented business process: request forms, purpose of change, scope, date/time, affected systems, **risk analysis**, rollback plan, sandbox testing, responsible staff, **change advisory board (CAB)** approval, end-user acceptance.

## Backups
| Type | Backs up | Archive bit cleared? | Restore needs |
|---|---|---|---|
| Full | Everything | Yes | Last full |
| Incremental | Changes since last backup (any) | Yes | Full + **all** incrementals |
| Differential | Changes since last **full** | No | Full + last differential |
| Synthetic full | Combines full + incrementals | — | One file |

- **3-2-1 rule**: 3 copies, 2 different media, 1 offsite.
- GFS rotation (Grandfather-Father-Son). Test restores regularly. On-site vs off-site/cloud.

## Safety
- **ESD**: wrist strap, mat, antistatic bags, ground yourself.
- Equipment grounding, disconnect power before repairs, proper lifting (bend knees), fire extinguisher (Class C for electrical), PPE (safety goggles, air filter mask), cable management.
- Power: surge suppressor, **UPS** (battery backup), brownouts vs blackouts vs surges.
- Environment: temperature, humidity, ventilation; **MSDS/SDS** for chemical handling and disposal; battery/toner/CRT disposal per local regulations.

## Privacy, licensing, policy
- Incident response: chain of custody, inform management/law enforcement, copy/preserve data, document incident.
- Licensing: DRM, EULA, open source vs commercial, personal vs corporate, valid licenses.
- Regulated data: PII, PCI DSS (credit cards), GDPR (EU), PHI/HIPAA (health), data retention requirements.

## Professionalism & communication
Proper attire, punctual, avoid distractions (no personal calls), active listening, don't interrupt, clarify the issue, set expectations & timelines, follow up, deal with confidential materials appropriately, don't argue or be judgmental, use plain language (no jargon).

## Scripting basics
| Extension | Language |
|---|---|
| .bat | Batch file (Windows) |
| .ps1 | PowerShell |
| .vbs | VBScript |
| .sh | Bash/shell (Linux/macOS) |
| .js | JavaScript |
| .py | Python |

Uses: automation, restarting machines, remapping drives, installing apps, backups, gathering info, updates. Risks: unintentionally introducing malware, changing system settings, crashing browsers/systems due to mishandled resources.

## Remote access
RDP (3389), VPN, VNC, SSH (22), RMM (remote monitoring & management), screen-sharing tools, desktop management, video conferencing. Security considerations for each.

## AI (new in V15)
Appropriate use, AI integration in apps, data privacy concerns (don't paste sensitive data into public AI), bias, hallucinations, accuracy, public vs private AI tools, AUP for AI.

## My notes
