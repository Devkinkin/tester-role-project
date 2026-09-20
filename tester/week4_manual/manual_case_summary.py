from collections import Counter
from pathlib import Path
import csv

CSV_PATH = Path(__file__).with_name("manual_test_cases.csv")

with CSV_PATH.open(newline="", encoding="utf-8") as file:
    cases = list(csv.DictReader(file))

print(f"Total cases: {len(cases)}")

coverage = Counter(case["Type"] for case in cases)

for test_type, count in sorted(coverage.items()):
    print(f"{test_type}: {count}")
