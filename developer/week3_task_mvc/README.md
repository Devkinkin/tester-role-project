# Week 3 – ASP.NET Core MVC + Docker Practice

What I practised:
- Model / View / Controller separation
- form submission
- model validation
- controller actions
- basic Docker containerisation

Run locally:
```powershell
dotnet restore
dotnet run
```

Optional Docker practice:
```powershell
docker build -t taskmvc-practice .
docker run --rm -p 8080:8080 taskmvc-practice
```
