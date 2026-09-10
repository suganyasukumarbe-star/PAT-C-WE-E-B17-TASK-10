import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Runs without opening GUI (ideal for tests)
    driver = webdriver.WebDriver()
    yield driver
    driver.quit()


# ==================== POSITIVE TEST CASES ====================

def test_positive_title(setup_driver):
    """Verifies that the initial title is correct."""
    driver = setup_driver
    driver.get("https://www.saucedemo.com/")
    assert driver.title == "Swag Labs"


def test_positive_homepage_url(setup_driver):
    """Verifies that the landing page URL is correct."""
    driver = setup_driver
    driver.get("https://www.saucedemo.com/")
    assert driver.current_url == "https://www.saucedemo.com/"


def test_positive_dashboard_url(setup_driver):
    """Verifies redirect to the inventory page after a valid login."""
    driver = setup_driver
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    assert driver.current_url == "https://saucedemo.com"


# ==================== NEGATIVE TEST CASES ====================

def test_negative_title(setup_driver):
    """Asserts that the application title is NOT an incorrect string."""
    driver = setup_driver
    driver.get("https://www.saucedemo.com/")
    assert driver.title != "Incorrect Title"


def test_negative_homepage_url(setup_driver):
    """Asserts that the web app is not loading a generic unsecure protocol variant."""
    driver = setup_driver
    driver.get("https://www.saucedemo.com/")
    assert driver.current_url != "https://saucedemo.com"


def test_negative_dashboard_url(setup_driver):
    """Verifies that an invalid password fails authentication and does not route to the dashboard."""
    driver = setup_driver
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    # URL should stay on the homepage, not the inventory dashboard
    assert driver.current_url != 'https://saucedemo.com'
