using OpenQA.Selenium;

namespace GroupApp.Tests.Pages;

public class HomePage
{
    private readonly IWebDriver _driver;

    public HomePage(IWebDriver driver)
    {
        _driver = driver;
    }

    public void Open(string baseUrl)
    {
        _driver.Navigate().GoToUrl(baseUrl);
    }

    public string Title => _driver.Title;

    public string BodyText =>
        _driver.FindElement(By.TagName("body")).Text;

    public int BrokenImageCount()
    {
        var images = _driver.FindElements(By.TagName("img"));
        var broken = 0;

        foreach (var image in images)
        {
            var isLoaded = (bool)((IJavaScriptExecutor)_driver).ExecuteScript(
                "return arguments[0].complete && arguments[0].naturalWidth > 0;",
                image
            );

            if (!isLoaded)
                broken++;
        }

        return broken;
    }
}
