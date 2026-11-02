# Windows Command-Line Tools

| Command | What it does |
|---|---|
| `ipconfig` / `ipconfig /all` | Show IP config (all = MAC, DNS, DHCP) |
| `ipconfig /release` · `/renew` · `/flushdns` | Drop/get DHCP lease; clear DNS cache |
| `ping` | Test reachability (`-t` continuous) |
| `tracert` | Show hops to destination |
| `pathping` | ping + tracert combined, shows packet loss per hop |
| `nslookup` | Query DNS |
| `netstat` | Active connections & listening ports (`-a`, `-n`, `-b`) |
| `net use` | Map network drive (`net use Z: \\server\share`) |
| `net user` | Manage user accounts |
| `hostname` | Show computer name |
| `cd`, `dir`, `md`, `rmdir` | Navigation & folders |
| `copy`, `xcopy`, `robocopy` | Copy files (robocopy = robust, resumable, mirrors) |
| `chkdsk` | Check disk (`/f` fix errors, `/r` locate bad sectors) |
| `sfc /scannow` | System File Checker — repair protected system files |
| `DISM /Online /Cleanup-Image /RestoreHealth` | Repair the Windows image (run before sfc if sfc fails) |
| `diskpart` | Partition management |
| `format` | Format a drive |
| `gpupdate /force` | Apply Group Policy now |
| `gpresult /r` | Show applied Group Policy |
| `shutdown /r /t 0` | Restart now (`/s` shutdown) |
| `winver` | Show Windows version |
| `whoami` | Show current user |
| `tasklist` / `taskkill /PID <n> /F` | List / kill processes |
| `bootrec /fixmbr` · `/fixboot` · `/rebuildbcd` | Repair boot (from recovery environment) |
| `[command] /?` | Help for any command |
