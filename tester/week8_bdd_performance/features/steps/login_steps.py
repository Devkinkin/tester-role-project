from behave import given, when, then
from selenium.webdriver.common.by import By


@given("I open the demo login page")
def open_login(context):
    context.driver.get(
        "https://the-internet.herokuapp.com/login"
    )


@when("I enter valid credentials")
def valid_credentials(context):
    context.driver.find_element(
        By.ID, "username"
    ).send_keys("tomsmith")

    context.driver.find_element(
        By.ID, "password"
    ).send_keys("SuperSecretPassword!")

    context.driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()


@when("I enter a valid username and an invalid password")
def invalid_password(context):
    context.driver.find_element(
        By.ID, "username"
    ).send_keys("tomsmith")

    context.driver.find_element(
        By.ID, "password"
    ).send_keys("wrong-password")

    context.driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()


@when("I submit empty credentials")
def empty_credentials(context):
    context.driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()


@then("I should reach the secure area")
def secure_area(context):
    assert "/secure" in context.driver.current_url


@then("I should see an invalid password message")
def password_error(context):
    message = context.driver.find_element(
        By.ID, "flash"
    ).text

    assert "Your password is invalid!" in message


@then("I should remain unauthenticated")
def remains_logged_out(context):
    assert "/login" in context.driver.current_url
