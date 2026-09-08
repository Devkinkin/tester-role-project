using GroupApp.Tests.Pages;
using NUnit.Framework;

namespace GroupApp.Tests.Tests;

[TestFixture]
public class HomePageTests : BaseTest
{
    [Test]
    public void Smoke_HomePage_Loads()
    {
        var page = new HomePage(Driver);
        page.Open(BaseUrl);

        Assert.That(Driver.Url, Does.StartWith(BaseUrl));
        Assert.That(page.BodyText, Is.Not.Empty);
    }

    [Test]
    public void Smoke_HomePage_HasTitle()
    {
        var page = new HomePage(Driver);
        page.Open(BaseUrl);

        Assert.That(page.Title, Is.Not.Null.And.Not.Empty);
    }

    [Test]
    public void Smoke_HomePage_HasNoBrokenImages()
    {
        var page = new HomePage(Driver);
        page.Open(BaseUrl);

        Assert.That(page.BrokenImageCount(), Is.EqualTo(0),
            "One or more images did not load correctly.");
    }
}
