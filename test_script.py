from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    print("Opening Homepage...")
    driver.get("https://www.intervue.io/")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(2)

    print("Navigating to Access Account page...")
    driver.get("https://www.intervue.io/access-account")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(2)

    print("Navigating to Login page...")
    driver.get("https://www.intervue.io/login")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "email")))
    time.sleep(2)

    print("Filling Email...")
    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys("neha@intervue.io")

    print("Filling Password...")
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys("Ps@neha@123")

    print("Clicking Login button...")
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Login with email']]"))
    )
    submit_button.click()

    print("Waiting for Dashboard to load fully...")
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.userAvatar"))
    )
    print("Dashboard loaded completely!")

    # --- Step 1: Wait until <div class="video-overlay"></div> is rendered ---
    print("Waiting for video overlay to render...")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.video-overlay"))
    )
    print("Video overlay rendered. Proceeding to search bar...")

    # --- Step 2: Click on Search Bar using visible text ---
    print("Clicking on search bar...")
    search_bar = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Search by candidate name')]"))
    )
    search_bar.click()
    time.sleep(2)  # Wait for the search bar to open up

    # --- Step 3: Wait for the search input to be visible before typing ---
    print("Waiting for search input to be visible...")
    search_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Type what you want to search for']"))
    )
    print("Typing 'hello' in search box...")
    search_input.send_keys("hello")
    time.sleep(3)  # Wait for dropdown to appear

    # --- Step 4: Select dropdown result ---
    print("Selecting dropdown result...")
    search_result = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'SearchThrough__PlaceholderText') and contains(., 'hello')]"))
    )
    search_result.click()

    # --- Step 5: Wait for redirection to search result page ---
    print("Waiting for search result page to load...")
    WebDriverWait(driver, 20).until(
        EC.url_contains("https://www.intervue.io/profile/search/interviews?query=hello")
    )
    print("Search result page loaded.")

    # --- Step 6: Open profile dropdown ---
    print("Clicking on profile avatar...")
    profile_avatar = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.userAvatar"))
    )
    profile_avatar.click()
    time.sleep(1)

    # --- Step 7: Click Logout ---
    print("Clicking Logout...")
    logout_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='Dropdown__DropdownItemLink-k60emx-2 hHnuKn' and text()='Logout']"))
    )
    logout_button.click()

    print("Logged out successfully.")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    time.sleep(3)
    driver.quit()
