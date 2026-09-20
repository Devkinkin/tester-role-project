from pathlib import Path
import csv
import math
import sys


def percentile(values, percentile_value):
    if not values:
        return 0.0

    ordered = sorted(values)
    rank = math.ceil(
        (percentile_value / 100) * len(ordered)
    ) - 1

    rank = min(max(rank, 0), len(ordered) - 1)

    return ordered[rank]


def summarise(csv_path):
    elapsed = []
    success_count = 0
    total = 0

    with Path(csv_path).open(
        newline="",
        encoding="utf-8"
    ) as file:

        for row in csv.DictReader(file):
            total += 1
            elapsed.append(float(row["elapsed"]))

            if row["success"].strip().lower() == "true":
                success_count += 1

    if total == 0:
        raise ValueError("No result rows found.")

    average = sum(elapsed) / total
    errors = total - success_count
    error_rate = (errors / total) * 100

    return {
        "samples": total,
        "average_ms": average,
        "p90_ms": percentile(elapsed, 90),
        "p95_ms": percentile(elapsed, 95),
        "errors": errors,
        "error_rate_percent": error_rate,
    }


if __name__ == "__main__":
    path = (
        sys.argv[1]
        if len(sys.argv) > 1
        else Path(__file__).with_name(
            "sample_jmeter_results.csv"
        )
    )

    result = summarise(path)

    print("Performance summary")
    print(f"Samples:    {result['samples']}")
    print(f"Average:    {result['average_ms']:.1f} ms")
    print(f"P90:        {result['p90_ms']:.1f} ms")
    print(f"P95:        {result['p95_ms']:.1f} ms")
    print(f"Errors:     {result['errors']}")
    print(
        f"Error rate: "
        f"{result['error_rate_percent']:.1f}%"
    )
