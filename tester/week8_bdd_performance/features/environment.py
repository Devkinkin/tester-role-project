from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    context.driver = webdriver.Chrome(options=options)


def after_scenario(context, scenario):
    context.driver.quit()
