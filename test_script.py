from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver_path = "C:\\Users\\vinee\\OneDrive\\Desktop\\career\\selenium-project\\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)

# Open website
driver.get("https://intervue.io/")

try:
    wait = WebDriverWait(driver, 10)

    # Click on "Login"
    login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
    login_button.click()

    # Click on "Login for Companies"
    company_login = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/login' and contains(@class, 'AccessAccount-ColoredButton')]")
    ))
    company_login.click()

    # Fill in credentials
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    email_input.send_keys("neha@intervue.io")
    password_input.send_keys("Ps@neha@123")

    # Click login
    submit = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Login')]")
    ))
    submit.click()

    # Wait to see if login succeeded or failed
    time.sleep(3)

    # Check for login failure by checking if still on login page
    if "login" in driver.current_url.lower():
        driver.save_screenshot("login_failed.png")
        print("Login failed. Screenshot saved.")
    else:
        print("Login successful.")

        # Proceed with test steps
        search_bar = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
        search_bar.send_keys("hello there")
        search_bar.send_keys(Keys.RETURN)
        time.sleep(3)

        # Click on profile icon
        profile_icon = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'dropdown-toggle')]")
        ))
        profile_icon.click()

        # Click Logout
        logout_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'Logout')]")
        ))
        logout_button.click()
        print("Logged out successfully.")

except Exception as e:
    print("Error occurred:", e)
    driver.save_screenshot("error.png")

finally:
    time.sleep(2)
    driver.quit()
