# Core 1 · Domain 5 — Hardware & Network Troubleshooting (28%)

**Biggest domain.** Start with [../cheat-sheets/troubleshooting-methodology.md](../cheat-sheets/troubleshooting-methodology.md).

## Motherboard / RAM / CPU / power
| Symptom | Likely cause |
|---|---|
| POST beeps | Check manufacturer beep codes (often RAM/video) |
| Blue screen (BSOD) / proprietary crash screens | Drivers, RAM, overheating |
| Random shutdowns | Overheating, failing PSU |
| No power | PSU, power switch, cable, outlet |
| Burning smell / smoke | Unplug immediately — PSU or component failure |
| Capacitor swelling | Replace motherboard |
| Date/time resets | CMOS battery |
| Fans spin, no display | RAM, CPU, video, monitor input |
| Grinding noise | Failing fan or HDD |

## Storage
- Clicking/grinding → failing HDD. **Back up data first.**
- S.M.A.R.T. errors → drive failing.
- Bootable device not found → boot order, failed drive, corrupted boot sector.
- RAID degraded / failure → replace failed drive and rebuild.
- Slow performance → fragmentation (HDD only), drive failing, full disk.

## Video / display
- No image → cable, input selection, brightness, power.
- Dim image → backlight; burn-in → OLED/plasma static images.
- Dead pixels, flickering (cable/refresh rate), incorrect color (cable/calibration), fuzzy (wrong resolution — use native).

## Mobile devices
- Poor battery health, swollen battery (**stop using; dispose properly**), broken screen, overheating, liquid damage.
- Digitizer issues / ghost touches, physically damaged ports, malware, cursor drift → calibrate touchpad.

## Printers
| Symptom | Cause |
|---|---|
| Lines down page | Dirty drum/print head |
| Garbled print | Wrong driver |
| Toner not fused / smears | Fuser |
| Paper jam | Rollers, wrong paper, obstruction |
| Faded print | Low toner/ink |
| Ghost images | Drum/cleaning |
| Double/creased paper | Pickup/separation rollers |
| Grinding noise | Gears, rollers |

## Network
| Symptom | Tool / cause |
|---|---|
| No connectivity | Check link lights, cable (cable tester), IP config (`ipconfig`) |
| 169.254.x.x | DHCP unreachable |
| Intermittent wireless | Interference, distance, channel overlap → Wi-Fi analyzer |
| Slow speeds | Duplex mismatch, interference, bandwidth saturation |
| Can ping IP but not hostname | **DNS** issue (`nslookup`) |
| Jitter / latency | VoIP quality issues, QoS |
| Port flapping | Bad cable / NIC |
| IP conflict | Duplicate static address |

## My notes
