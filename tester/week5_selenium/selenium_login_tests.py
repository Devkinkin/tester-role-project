import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tester.week5_selenium.login_page import LoginPage


class LoginTests(unittest.TestCase):
    BASE_URL = "https://the-internet.herokuapp.com"

    def setUp(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,1000")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
        self.page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_01_login_page_loads(self):
        self.page.open(self.BASE_URL)
        self.assertTrue(self.page.is_loaded())

    def test_02_valid_login(self):
        self.page.open(self.BASE_URL)
        self.page.login("tomsmith", "SuperSecretPassword!")
        self.assertIn("/secure", self.driver.current_url)

    def test_03_invalid_password(self):
        self.page.open(self.BASE_URL)
        self.page.login("tomsmith", "wrong-password")
        self.assertIn("Your password is invalid!", self.page.message())

    def test_04_invalid_username(self):
        self.page.open(self.BASE_URL)
        self.page.login("not-a-user", "SuperSecretPassword!")
        self.assertIn("Your username is invalid!", self.page.message())

    def test_05_empty_credentials(self):
        self.page.open(self.BASE_URL)
        self.page.login("", "")
        self.assertIn("Your username is invalid!", self.page.message())


if __name__ == "__main__":
    unittest.main(verbosity=2)
