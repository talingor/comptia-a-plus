# CompTIA A+ Study Repo

My personal study hub for passing the **CompTIA A+ (V15)** certification: notes, cheat sheets, flashcards, a practice quiz, and hands-on labs.

> Always confirm the current objectives at [comptia.org](https://www.comptia.org/certifications/a) — download the official exam objectives PDF and keep it next to this repo.

## The exams

| | Core 1 (220-1201) | Core 2 (220-1202) |
|---|---|---|
| Questions | Max 90 (multiple choice + performance-based) | Max 90 (multiple choice + performance-based) |
| Time | 90 minutes | 90 minutes |
| Passing score | 675 (scale 100–900) | 700 (scale 100–900) |

You must pass **both** to earn A+.

### Core 1 domains
| # | Domain | Weight | Notes |
|---|---|---|---|
| 1 | Mobile Devices | 13% | [core-1/01-mobile-devices.md](core-1/01-mobile-devices.md) |
| 2 | Networking | 23% | [core-1/02-networking.md](core-1/02-networking.md) |
| 3 | Hardware | 25% | [core-1/03-hardware.md](core-1/03-hardware.md) |
| 4 | Virtualization & Cloud Computing | 11% | [core-1/04-virtualization-cloud.md](core-1/04-virtualization-cloud.md) |
| 5 | Hardware & Network Troubleshooting | 28% | [core-1/05-troubleshooting.md](core-1/05-troubleshooting.md) |

### Core 2 domains
| # | Domain | Weight | Notes |
|---|---|---|---|
| 1 | Operating Systems | 28% | [core-2/01-operating-systems.md](core-2/01-operating-systems.md) |
| 2 | Security | 28% | [core-2/02-security.md](core-2/02-security.md) |
| 3 | Software Troubleshooting | 23% | [core-2/03-software-troubleshooting.md](core-2/03-software-troubleshooting.md) |
| 4 | Operational Procedures | 21% | [core-2/04-operational-procedures.md](core-2/04-operational-procedures.md) |

## Repo layout

```
core-1/          Notes per Core 1 domain
core-2/          Notes per Core 2 domain
cheat-sheets/    Must-memorize tables (ports, Wi-Fi, RAID, commands, troubleshooting steps)
flashcards/      CSV decks — import into Anki or Quizlet
practice/        Command-line quiz (python3 practice/quiz.py)
labs/            Hands-on exercises to do on a real/virtual machine
STUDY-PLAN.md    8-week schedule
PROGRESS.md      Checklist + practice-test score log
```

## How to use it

1. Follow [STUDY-PLAN.md](STUDY-PLAN.md) week by week.
2. Expand each notes file in your own words as you study — that's where the learning happens.
3. Drill the [cheat sheets](cheat-sheets/) daily until they're automatic.
4. Run the quiz: `python3 practice/quiz.py` (or `python3 practice/quiz.py --core 2 -n 20`).
5. Log every practice exam in [PROGRESS.md](PROGRESS.md). Book the real exam once you consistently score **85%+**.
6. Commit daily — your green GitHub contribution graph doubles as a study streak.
