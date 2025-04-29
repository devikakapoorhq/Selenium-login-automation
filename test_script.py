from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")

# Path to chromedriver
chrome_driver_path = r"C:\Users\vinee\OneDrive\Desktop\career\selenium-project\chromedriver.exe"
  # <- Update this
service = Service(chrome_driver_path)

# Open browser
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

try:
    # Step 1: Go directly to the login page
    driver.get("https://www.intervue.io/login")
    wait = WebDriverWait(driver, 20)

    # Step 2: Wait and enter credentials
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    email_input.send_keys("neha@intervue.io")
    password_input.send_keys("Ps@neha@123")

    # Step 3: Click login button
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]")))
    login_btn.click()

    # Step 4: Wait for navigation
    time.sleep(5)  # You can replace with WebDriverWait for dashboard elements

    print("Final URL after login:", driver.current_url)
    if "dashboard" in driver.current_url.lower():
        print("✅ Login successful!")
    else:
        print("❌ Login failed or redirected elsewhere.")

except Exception as e:
    print("❗ Error:", str(e))
    traceback.print_exc()

finally:
    time.sleep(5)
    driver.quit()
