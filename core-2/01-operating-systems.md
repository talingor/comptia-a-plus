# Core 2 · Domain 1 — Operating Systems (28%)

## Windows editions (10/11)
| Feature | Home | Pro | Enterprise/Education |
|---|---|---|---|
| Join domain / Group Policy (gpedit.msc) | ❌ | ✅ | ✅ |
| BitLocker | ❌ (Device Encryption only) | ✅ | ✅ |
| Remote Desktop **host** | ❌ (client only) | ✅ | ✅ |
| Hyper-V | ❌ | ✅ | ✅ |

Windows 11 requirements: 64-bit CPU (1 GHz, 2+ cores), 4 GB RAM, 64 GB storage, **TPM 2.0**, **UEFI + Secure Boot**.

## Installation
- Boot methods: USB, network (PXE), ISO, internal partition (recovery), external drive.
- Types: clean install, in-place upgrade, image deployment, repair install, remote network install, zero-touch.
- Partitioning: **MBR** (max 4 primary partitions, 2 TB) vs **GPT** (UEFI, 128 partitions, huge disks).
- File systems: **NTFS** (Windows, permissions, encryption), **FAT32** (4 GB file limit), **exFAT** (flash drives, large files), **ReFS**, **ext4** (Linux), **APFS** (macOS), XFS.

## Windows tools (know the .msc / .exe names)
| Tool | Command |
|---|---|
| Computer Management | compmgmt.msc |
| Device Manager | devmgmt.msc |
| Disk Management | diskmgmt.msc |
| Event Viewer | eventvwr.msc |
| Task Scheduler | taskschd.msc |
| Services | services.msc |
| Local Users & Groups | lusrmgr.msc |
| Group Policy Editor | gpedit.msc |
| Certificate Manager | certmgr.msc |
| Performance Monitor | perfmon.msc |
| System Configuration | msconfig.exe |
| System Information | msinfo32.exe |
| Resource Monitor | resmon.exe |
| Registry Editor | regedit.exe |
| Disk Cleanup | cleanmgr.exe |
| Defragment/Optimize | dfrgui.exe |
| DirectX Diagnostic | dxdiag.exe |

Command-line tools: see [../cheat-sheets/windows-commands.md](../cheat-sheets/windows-commands.md).

## Networking in Windows
Workgroup vs domain; shared resources & mapped drives (`net use`); firewall settings; proxy settings; metered connections; static IP config.

## macOS
Finder, Spotlight, Keychain, iCloud, Time Machine (backup), Disk Utility, Terminal, Mission Control, Boot Camp (Intel only), FileVault (encryption), .dmg / .pkg / .app install files, System Settings.

## Linux
| Command | Purpose |
|---|---|
| ls, cd, pwd, mv, cp, rm | Files & navigation |
| chmod / chown | Permissions / ownership |
| sudo / su | Elevated privileges |
| apt / dnf (yum) | Package managers |
| grep, find | Search |
| ps, top | Processes |
| ip / ifconfig, ping, dig | Networking |
| df / du | Disk space |
| nano, vi | Editors |
| cat, man | View files / manual |
| fsck / mount | Filesystem check / mount |

## Application installation
Check system requirements (CPU, 32 vs 64-bit, RAM, storage, GPU), distribution method (physical media, download, ISO mountable), impact on device/network/user/business.

## My notes
