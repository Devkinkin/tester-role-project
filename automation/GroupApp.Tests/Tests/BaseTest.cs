using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace GroupApp.Tests.Tests;

public abstract class BaseTest
{
    protected IWebDriver Driver = null!;
    protected string BaseUrl = null!;

    [SetUp]
    public void SetUp()
    {
        BaseUrl = Environment.GetEnvironmentVariable("BASE_URL")
                  ?? "http://localhost:5000";

        var options = new ChromeOptions();
        options.AddArgument("--start-maximized");

        Driver = new ChromeDriver(options);
        Driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(3);
    }

    [TearDown]
    public void TearDown()
    {
        Driver?.Quit();
        Driver?.Dispose();
    }
}
