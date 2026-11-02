# Ports & Protocols — MEMORIZE

| Port | Protocol | TCP/UDP | Purpose |
|---|---|---|---|
| 20, 21 | FTP | TCP | File transfer (20 data, 21 control) |
| 22 | SSH / SFTP | TCP | Secure remote shell, secure file transfer |
| 23 | Telnet | TCP | Insecure remote shell |
| 25 | SMTP | TCP | Send email |
| 53 | DNS | TCP/UDP | Name resolution |
| 67, 68 | DHCP | UDP | IP address assignment (67 server, 68 client) |
| 80 | HTTP | TCP | Web |
| 110 | POP3 | TCP | Retrieve email (downloads) |
| 137–139 | NetBIOS/NetBT | TCP/UDP | Legacy Windows name/file sharing |
| 143 | IMAP | TCP | Retrieve email (syncs) |
| 161, 162 | SNMP | UDP | Network management (162 = traps) |
| 389 | LDAP | TCP/UDP | Directory services |
| 443 | HTTPS | TCP | Secure web |
| 445 | SMB/CIFS | TCP | Windows file/printer sharing |
| 3389 | RDP | TCP | Remote Desktop |

Also good to know: 69 TFTP (UDP), 88 Kerberos, 123 NTP (UDP), 514 Syslog (UDP), 587 SMTP submission, 636 LDAPS, 993 IMAPS, 995 POP3S.

## Memory tricks
- **21** FTP "file-two-one" · **22** SSH "secure-secure" · **23** Telnet "tell-a-three"
- **25** SMTP — "Send Mail To People" (25¢ stamp)
- **53** DNS — "Domain Name, 5-3"
- **67/68** DHCP — server first (lower), client second
- **110** POP3 vs **143** IMAP — POP is smaller number = older, simpler
- **443** = **80** + secure
- **445** SMB — right after HTTPS
- **3389** RDP — the only big one you need
