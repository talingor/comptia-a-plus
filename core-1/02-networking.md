# Core 1 · Domain 2 — Networking (23%)

## Ports & protocols
See [../cheat-sheets/ports-protocols.md](../cheat-sheets/ports-protocols.md). Know port **and** TCP/UDP.

## TCP vs UDP
- **TCP**: connection-oriented, 3-way handshake (SYN, SYN-ACK, ACK), guaranteed delivery.
- **UDP**: connectionless, fast, no guarantee (DNS queries, DHCP, VoIP, streaming, TFTP).

## Networking hardware
| Device | What it does |
|---|---|
| Router | Connects different networks (Layer 3, IP addresses) |
| Switch (managed/unmanaged) | Connects devices on same network (Layer 2, MAC addresses); managed = VLANs, port config |
| Access point | Bridges wireless clients onto wired network |
| Patch panel | Cable termination point in a rack |
| Firewall | Filters traffic by rules |
| PoE / PoE injector | Power over Ethernet (802.3af 15.4W, 802.3at PoE+ 30W, 802.3bt up to 60–100W) |
| Cable modem / DSL modem / ONT | ISP connection (coax / phone line / fiber) |
| NIC | Network interface card |

## Wireless
See [../cheat-sheets/wifi-standards.md](../cheat-sheets/wifi-standards.md).
- 2.4 GHz: longer range, more interference; non-overlapping channels **1, 6, 11**.
- 5 GHz: faster, shorter range, more channels. 6 GHz: Wi-Fi 6E/7.
- Bluetooth, NFC, RFID; long-range fixed wireless.

## Services
- **DHCP**: assigns IPs — DORA (Discover, Offer, Request, Acknowledge). Scopes, reservations, exclusions, lease time.
- **DNS** records: A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), TXT (SPF, DKIM, DMARC for email security).
- Others: file share, print server, mail server, syslog, web server, AAA (RADIUS/TACACS+), proxy, load balancer, UTM, SCADA/ICS, IoT.

## IP addressing
- IPv4 private ranges: **10.0.0.0/8**, **172.16.0.0–172.31.255.255 (/12)**, **192.168.0.0/16**.
- **APIPA**: 169.254.x.x → DHCP failed.
- Loopback: 127.0.0.1 (IPv4), ::1 (IPv6).
- IPv6: 128-bit, hex, `::` compresses zeros; link-local starts with **fe80::**.
- Static vs dynamic; default gateway; subnet mask; VLAN; VPN.

## Network types
PAN < LAN < MAN < WAN; WLAN; SAN (storage).
Internet connections: satellite (high latency), fiber, cable, DSL, cellular, fixed wireless.

## Tools
Crimper, cable stripper, cable tester, toner probe, punchdown tool, loopback plug, Wi-Fi analyzer, network tap.

## Cabling
- Cat 5e (1 Gbps), Cat 6 (10 Gbps ≤55m), Cat 6a (10 Gbps 100m), Cat 8 (25–40 Gbps, 30m, data centers).
- Plenum vs PVC (plenum = fire-resistant, for air-handling spaces). STP vs UTP. Direct burial.
- T568A / T568B wiring — B: white-orange, orange, white-green, blue, white-blue, green, white-brown, brown.
- Fiber: single-mode (long distance, laser) vs multimode (shorter, LED). Connectors: SC, LC, ST.
- Coax: RG-6 (cable TV/internet), F-connector.

## My notes
