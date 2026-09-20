# Kinley – Complete Individual Contribution

This repository pack covers my individual contribution from the beginning of the unit.

## Phase 1 – Developer (Weeks 1–3)

My developer learning was .NET-based, so these folders are **C#/.NET**, not Python:

- Week 1: C# + SQLite CRUD task console
- Week 2: ASP.NET Core Web API + EF Core
- Week 3: ASP.NET Core MVC + Docker basics

## Phase 2 – Tester / QA (Weeks 4–10)

My tester practice includes Python and testing tools:

- Week 4: manual testing
- Week 5: Selenium Python
- Week 6: API / HTTP testing with Python
- Week 7: regression + CI concepts
- Week 8: BDD + performance analysis
- Week 9: QA reporting
- Week 10: planned finalisation

## Python setup

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Useful Python commands

```powershell
python tester/week4_manual/manual_case_summary.py

python -m unittest tester.week5_selenium.selenium_login_tests -v

python tester/week6_api_testing/api_tests.py

python tester/week6_api_testing/http_response_inspector.py

python tester/week7_regression_ci/regression_runner.py

python tester/week7_regression_ci/ci_smoke_check.py

behave tester/week8_bdd_performance/features

python tester/week8_bdd_performance/jmeter_results_summary.py

python tester/week9_reporting/weekly_qa_summary.py
```

## Important

The developer phase stays in C# because that is what I was learning at that stage.
I have not converted the developer work into Python because doing that would not match my actual role progression.
