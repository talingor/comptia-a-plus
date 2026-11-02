# Lab 2 — Build a Virtual Lab

1. Confirm virtualization is enabled (Task Manager → Performance → CPU → "Virtualization: Enabled").
2. Install a Type 2 hypervisor: **VirtualBox** (free) or Hyper-V (Windows Pro).
3. Create VMs:
   - Windows 11 evaluation ISO (free from Microsoft Evaluation Center) — note TPM/Secure Boot settings needed.
   - Ubuntu Desktop.
4. Take a **snapshot**, break something (delete a system file, change a setting), then revert.
5. Try each network mode: NAT, bridged, host-only. Run `ipconfig` / `ip a` in each and note the IP differences.

You'll reuse these VMs for Labs 3+ and Core 2.
