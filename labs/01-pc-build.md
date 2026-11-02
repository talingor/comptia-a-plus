# Lab 1 — Know Your Hardware

No spare PC? Use a virtual PC builder (e.g., PC Building Simulator) or teardown videos alongside these steps.

1. Put on an ESD strap (or touch bare chassis metal), unplug power.
2. Open a desktop. Identify and photograph: motherboard form factor, CPU socket, RAM slots (DDR4/DDR5?), PCIe slots, SATA ports, M.2 slots, CMOS battery, PSU connectors (24-pin, 8-pin CPU, PCIe).
3. Remove and reseat one RAM stick and one expansion card.
4. Boot into BIOS/UEFI. Find: boot order, Secure Boot, TPM, virtualization (VT-x/AMD-V), admin password.
5. In Windows, run `msinfo32` and `dxdiag`. Compare to what you saw physically.

**Write up** what you found in `core-1/03-hardware.md` → "My notes".
