# Core 2 · Domain 3 — Software Troubleshooting (23%)

## Windows OS issues
| Symptom | Try |
|---|---|
| BSOD | Check Event Viewer, recent driver/update, Safe Mode, System Restore |
| Slow performance | Task Manager / Resource Monitor, startup items, malware scan, disk space, add RAM |
| Boot problems | Startup Repair, Safe Mode, `bootrec`, check boot order |
| Frequent shutdowns | Overheating, power settings |
| Services not starting | services.msc, dependencies, Event Viewer |
| App crashes | Repair/reinstall, update, compatibility mode |
| Low memory warnings | Close apps, adjust virtual memory |
| USB controller resource warnings | Move devices to another controller |
| System instability / no OS found | Boot order, rebuild boot config |
| Slow profile load | Rebuild user profile |
| Time drift | CMOS battery, NTP |

Fixes ladder: reboot → restart services → uninstall/reinstall/update app → add resources → verify requirements → `sfc /scannow` → repair Windows → restore (System Restore) → reimage → roll back updates → rebuild profile.

## Security issues (symptoms of infection)
Pop-ups, browser redirects, security alerts from fake AV, slow performance, internet connectivity issues, PC/OS instability, desktop alerts, OS update failures, files renamed/encrypted/deleted, unwanted notifications, certificate warnings, hijacked email (contacts receive spam).

## ⭐ Malware removal — 7 steps (memorize in order)
1. **Investigate and verify** malware symptoms.
2. **Quarantine** infected systems (disconnect from network).
3. **Disable System Restore** (Windows) — restore points may be infected.
4. **Remediate**: update anti-malware software, scan & removal (Safe Mode / preinstallation environment).
5. **Schedule scans and run updates**.
6. **Enable System Restore** and create a restore point.
7. **Educate the end user**.

## Mobile OS & app issues
App fails to launch/close/update, slow to respond, OS fails to update, battery drain, random reboots, Bluetooth/Wi-Fi/NFC connectivity, screen won't autorotate.
Fixes: restart, force-stop, clear cache, update, reinstall, factory reset (last resort).

## Mobile security issues
Unexpected high data usage, fake security warnings, app from untrusted source (sideloading/APK), developer mode, rooting/jailbreaking, bootleg apps, unexpected app behavior, leaked personal files.

## My notes
