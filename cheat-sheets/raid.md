# RAID Levels

| Level | Name | Min drives | Fault tolerance | Usable capacity |
|---|---|---|---|---|
| **0** | Striping | 2 | ❌ None — one drive dies, all data lost | 100% |
| **1** | Mirroring | 2 | ✅ 1 drive | 50% |
| **5** | Striping w/ parity | 3 | ✅ 1 drive | (n−1) drives |
| **6** | Striping w/ double parity | 4 | ✅ 2 drives | (n−2) drives |
| **10** (1+0) | Stripe of mirrors | 4 | ✅ 1 per mirror pair | 50% |

Tricks:
- RAID **0** = **zero** fault tolerance
- RAID **1** = **one** copy of everything (mirror)
- RAID **5** = needs at least 3; lose **one** drive's worth to parity
- RAID **10** = 1 + 0 = mirror then stripe, needs 4

**RAID is not a backup.**
