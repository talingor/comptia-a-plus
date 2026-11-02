#!/usr/bin/env python3
"""CompTIA A+ command-line practice quiz.

Usage:
  python3 practice/quiz.py              # 10 random questions from both cores
  python3 practice/quiz.py --core 1 -n 20
  python3 practice/quiz.py --domain security
  python3 practice/quiz.py --missed     # retry questions you got wrong last time

Add your own questions to practice/questions.json.
"""
import argparse
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
QUESTIONS = HERE / "questions.json"
MISSED = HERE / ".missed.json"
LETTERS = "ABCDEFGH"


def load(path, default):
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def main():
    p = argparse.ArgumentParser(description="CompTIA A+ practice quiz")
    p.add_argument("--core", type=int, choices=[1, 2])
    p.add_argument("--domain", help="filter by domain name (partial match)")
    p.add_argument("-n", type=int, default=10, help="number of questions")
    p.add_argument("--missed", action="store_true", help="only questions missed last run")
    args = p.parse_args()

    pool = load(QUESTIONS, [])
    if args.missed:
        missed = set(load(MISSED, []))
        pool = [q for q in pool if q["q"] in missed]
    if args.core:
        pool = [q for q in pool if q["core"] == args.core]
    if args.domain:
        pool = [q for q in pool if args.domain.lower() in q["domain"].lower()]
    if not pool:
        print("No questions match those filters.")
        return

    picks = random.sample(pool, min(args.n, len(pool)))
    correct, wrong = 0, []
    by_domain = {}

    for i, q in enumerate(picks, 1):
        # Shuffle answer order so you learn the content, not the letter
        order = list(range(len(q["choices"])))
        random.shuffle(order)
        print(f"\n[{i}/{len(picks)}] (Core {q['core']} · {q['domain']})")
        print(q["q"])
        for letter, idx in zip(LETTERS, order):
            print(f"  {letter}) {q['choices'][idx]}")
        valid = LETTERS[: len(order)]
        ans = ""
        while ans not in valid:
            ans = input("Answer: ").strip().upper()[:1]
        chosen = order[valid.index(ans)]
        stats = by_domain.setdefault(q["domain"], [0, 0])
        stats[1] += 1
        if chosen == q["answer"]:
            correct += 1
            stats[0] += 1
            print("✅ Correct!")
        else:
            right = LETTERS[order.index(q["answer"])]
            print(f"❌ Wrong — answer: {right}) {q['choices'][q['answer']]}")
            wrong.append(q["q"])
        if q.get("why"):
            print(f"   💡 {q['why']}")

    pct = 100 * correct / len(picks)
    print(f"\nScore: {correct}/{len(picks)} ({pct:.0f}%)")
    for d, (c, t) in sorted(by_domain.items()):
        print(f"  {d:28} {c}/{t}")
    MISSED.write_text(json.dumps(wrong))
    if wrong:
        print("\nRetry what you missed: python3 practice/quiz.py --missed")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nBye!")
