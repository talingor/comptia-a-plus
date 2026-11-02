# Core 1 · Domain 3 — Hardware (25%)

## Cables & connectors
- Video: HDMI, DisplayPort, DVI (DVI-D digital, DVI-I both), VGA (analog, DB-15).
- USB: USB 2.0 (480 Mbps), USB 3.x (5/10/20 Gbps), USB4 (40/80 Gbps), USB-C connector; Thunderbolt 3/4/5 uses USB-C.
- Storage: SATA (6 Gbps), eSATA, SAS, M.2 (SATA or NVMe), NVMe (PCIe).
- Lightning (Apple), serial (DB-9), Molex.

## RAM
- DDR4 (288-pin), DDR5 (288-pin, different key notch, on-die ECC); SODIMM for laptops.
- **ECC** = error correction (servers). Single/dual/quad channel — install in matched pairs per manual.
- Virtual RAM = page file on disk.

## Storage
- HDD: 5,400 / 7,200 / 10,000 / 15,000 RPM; 2.5" and 3.5".
- SSD: SATA, M.2 (key B/M), NVMe (fastest, PCIe), mSATA (legacy).
- Flash drives, SD cards, optical (CD/DVD/Blu-ray).
- RAID: see [../cheat-sheets/raid.md](../cheat-sheets/raid.md).

## Motherboards
- Form factors: ATX, microATX, mini-ITX.
- Expansion: PCIe (x1, x4, x8, x16), PCI (legacy).
- Headers: power, USB, fan, audio, front panel.
- BIOS/UEFI: boot order, passwords, Secure Boot, TPM, virtualization support (VT-x/AMD-V), fan settings.
- **TPM** = hardware chip storing encryption keys (BitLocker; Windows 11 needs TPM 2.0). **HSM** = dedicated crypto device.
- CMOS battery (CR2032) — clock resets → battery dead.

## CPUs
- x86/x64 (Intel, AMD) vs ARM (mobile, Apple Silicon). Multicore, hyperthreading/SMT.
- Socket types (LGA = pins on board, PGA = pins on CPU). Thermal paste + heat sink/fan, liquid cooling.

## Expansion cards
Sound, video (GPU), capture, NIC, Wi-Fi.

## Power supplies
- 120V/240V input; 3.3V, 5V, 12V outputs. 24-pin ATX motherboard, 8-pin EPS CPU, 6/8-pin or 12VHPWR PCIe.
- Modular vs non-modular; redundant PSUs (servers). Wattage rating.

## Printers
| Type | Key points |
|---|---|
| **Laser** | Steps: **Processing, Charging, Exposing, Developing, Transferring, Fusing, Cleaning**. Fuser = heat (toner smears → fuser). Imaging drum, transfer belt/roller, pickup rollers, duplexing assembly. |
| **Inkjet** | Ink cartridges, print head, roller, feeder, carriage + belt. Clean/align heads. |
| **Thermal** | Heat-sensitive paper (receipts), heating element. |
| **Impact** | Dot matrix, multipart forms, print head, ribbon, tractor feed. |
| **3D** | Filament or resin, layer by layer. |

Printer config: drivers (PCL vs PostScript), duplex, orientation, tray, quality; sharing (USB, Ethernet, Wi-Fi, cloud); secure print, badging, audit logs.

Mnemonic for laser: **"People Can't Expect Dogs To Fly Correctly"**.

## My notes
