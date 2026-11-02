# Lab 3 — Windows Command Line & Tools

In your Windows VM, open Command Prompt **as administrator** and run each, noting what you see:

```
ipconfig /all
ipconfig /flushdns
ping -n 4 8.8.8.8
tracert google.com
nslookup google.com
netstat -an
whoami
hostname
winver
sfc /scannow
chkdsk C:
gpresult /r
tasklist
```

Then open each with Win+R: `compmgmt.msc`, `devmgmt.msc`, `diskmgmt.msc`, `eventvwr.msc`, `services.msc`, `taskschd.msc`, `lusrmgr.msc`, `msconfig`, `regedit`, `resmon`, `perfmon`.

Challenges:
1. Create a local standard user, then make it an administrator.
2. Create a shared folder; set share permission = Read, NTFS = Full Control. Access it from another VM. What's the effective permission?
3. Shrink C: in Disk Management and create a new exFAT partition.
4. Find the last unexpected shutdown in Event Viewer (System log, Event ID 6008).
