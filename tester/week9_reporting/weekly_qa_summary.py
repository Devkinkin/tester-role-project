from dataclasses import dataclass


@dataclass
class WeekSummary:
    week: str
    focus: str
    practical_work: str
    next_step: str


SUMMARIES = [
    WeekSummary(
        "Week 4",
        "Manual testing",
        "15 login cases and defect structure",
        "Automate a stable subset"
    ),
    WeekSummary(
        "Week 5",
        "Selenium automation",
        "Five login tests using a Page Object",
        "Add API-level checks"
    ),
    WeekSummary(
        "Week 6",
        "API/network testing",
        "Requests, assertions and HTTP inspection",
        "Build a regression pack"
    ),
    WeekSummary(
        "Week 7",
        "Regression and CI",
        "Regression runner and CI smoke check",
        "Add BDD and performance work"
    ),
    WeekSummary(
        "Week 8",
        "BDD and performance",
        "Gherkin scenarios and metrics summary",
        "Prepare final reporting"
    ),
    WeekSummary(
        "Week 9",
        "Reporting and consolidation",
        "QA progress summary and repository clean-up",
        "Final regression and retesting"
    ),
]


if __name__ == "__main__":
    print("QA Learning Summary")
    print("=" * 60)

    for item in SUMMARIES:
        print(f"\n{item.week}")
        print(f"Focus:          {item.focus}")
        print(f"Practical work: {item.practical_work}")
        print(f"Next step:      {item.next_step}")
