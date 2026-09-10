import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def perform_web_scraping():
    # Initialize Chrome Driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.WebDriver()

    try:
        # Navigate to the site
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)  # Allow page loading

        # 1) Fetch Title & 2) Current URL before login
        print(f"Pre-login Title: {driver.title}")
        print(f"Pre-login URL: {driver.current_url}")

        # Perform Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)  # Wait for dashboard transition

        # Post-login validations
        final_title = driver.title
        final_url = driver.current_url
        print(f"Post-login Title: {final_title}")
        print(f"Post-login URL: {final_url}")

        # 3) Extract entire contents (HTML page source)
        page_contents = driver.page_source

        # Save to Text file
        with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
            file.write(page_contents)
        print("Webpage contents successfully saved to 'Webpage_task_11.txt'")

    finally:
        driver.quit()


if __name__ == "__main__":
    perform_web_scraping()
