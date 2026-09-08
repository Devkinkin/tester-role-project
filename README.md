# Group App – Tester Starter Pack

This repository contains a realistic two-week testing starter pack for a .NET group project.

## What is included
- Manual smoke / functional test cases
- C# + NUnit + Selenium starter automation
- Page Object Model example
- Postman collection with basic assertions
- JMeter starter load test
- Defect report template
- Short SoapUI and LoadRunner setup notes

## Important
The test assets are intentionally generic because the group's exact pages and API routes may change.
Update `BASE_URL`, selectors, and API paths to match the actual application before reporting test results.

## Selenium quick start
1. Open `automation/GroupApp.Tests` in Visual Studio.
2. Restore NuGet packages.
3. Set the test application URL.

PowerShell:
```powershell
$env:BASE_URL="https://localhost:5001"
dotnet test
```

If `BASE_URL` is not set, tests default to `http://localhost:5000`.

## What to tell the team
Week 1:
- Defined the tester workflow and baseline manual coverage.
- Created a C# Selenium/NUnit automation project.
- Added a reusable BaseTest and Page Object Model starter.

Week 2:
- Added Postman API smoke checks.
- Added a JMeter load-test starter.
- Added defect reporting and regression/UAT preparation.
- Continued ISTQB and ITIL Foundation learning.

## Next
- Replace generic selectors with real project selectors.
- Add tests for the team's highest-risk feature.
- Add the real API endpoints to Postman.
- Execute the JMeter plan in the test environment.
