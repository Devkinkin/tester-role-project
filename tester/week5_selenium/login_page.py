from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8)

    def open(self, base_url):
        self.driver.get(f"{base_url}/login")

    def is_loaded(self):
        return (
            self.driver.find_element(*self.USERNAME).is_displayed()
            and self.driver.find_element(*self.PASSWORD).is_displayed()
            and self.driver.find_element(*self.SUBMIT).is_displayed()
        )

    def login(self, username, password):
        username_box = self.driver.find_element(*self.USERNAME)
        password_box = self.driver.find_element(*self.PASSWORD)

        username_box.clear()
        username_box.send_keys(username)

        password_box.clear()
        password_box.send_keys(password)

        self.driver.find_element(*self.SUBMIT).click()

    def message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.FLASH)
        ).text
