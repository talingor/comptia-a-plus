# Core 1 · Domain 4 — Virtualization & Cloud Computing (11%)

## Virtualization
- **Type 1 hypervisor** (bare metal): runs directly on hardware — VMware ESXi, Microsoft Hyper-V (server), Proxmox, Xen.
- **Type 2 hypervisor** (hosted): runs on an OS — VirtualBox, VMware Workstation, Parallels.
- Requirements: CPU virtualization support enabled in BIOS/UEFI (VT-x/AMD-V), enough RAM, storage, network.
- Uses: sandbox, test/dev, legacy software, cross-platform.
- **Containers** (e.g., Docker): share host kernel, lighter than VMs.
- VDI: virtual desktop infrastructure (desktops hosted centrally).
- Security: VM escape, VM sprawl, need to patch guest OSes too.

## Cloud models
| Service | You manage | Example |
|---|---|---|
| **IaaS** | OS, apps, data | AWS EC2, Azure VMs |
| **PaaS** | Apps, data | Heroku, Azure App Service |
| **SaaS** | Just use it | Microsoft 365, Gmail |

Deployment: **Public, Private, Hybrid, Community**.

Characteristics: shared resources, metered utilization, **rapid elasticity**, high availability, file synchronization, multitenancy, ingress/egress costs.

## My notes
