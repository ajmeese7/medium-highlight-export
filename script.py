import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from dotenv import load_dotenv
import os

load_dotenv()
chromedriver_autoinstaller.install()
browser = uc.Chrome()

###
# Navigate to the Medium login page and select the "Google" button
###
browser.get("https://medium.com/")
login_path = "//*[contains(text(), 'Sign In')]"
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, login_path)))
login_button = browser.find_element("xpath", login_path)
login_button.click()
login_with_google = "//*[contains(text(), 'Sign in with Google')]"
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, login_with_google)))
google_button = browser.find_element("xpath", login_with_google)
google_button.click()

###
# Log in to Google
###

# Enter username
username_path = "//input[@type='email']"
WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, username_path)))
username_input = browser.find_element("xpath", username_path)
username_input.send_keys(os.getenv("GOOGLE_USERNAME"))

# Click next
next_button_path = "//span[contains(text(), 'Next')]"
WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, next_button_path)))
next_button = browser.find_element("xpath", next_button_path)
next_button.click()

# Enter password
password_path = "//input[@type='password']"
WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, password_path)))
password_input = browser.find_element("xpath", password_path)
password_input.send_keys(os.getenv("GOOGLE_PASSWORD"))

# Login
login_button_path = "//span[contains(text(), 'Next')]"
WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, login_button_path)))
login_button = browser.find_element("xpath", login_button_path)
login_button.click()

###
# NOTE: You may have to confirm your identity here, but don't stress,
#       the script will continue as expected after you do so.
#       This code gives you a 60 second window to confirm your identity.
###

# Open the "lists" page
list_button_path = "//a[@href='/me/lists']"
WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.XPATH, list_button_path)))
list_button = browser.find_element("xpath", list_button_path)
list_button.click()

# Open the "highlights" tab
highlight_button_path = "//span[contains(text(), 'Highlights')]"
WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, highlight_button_path)))
highlight_button = browser.find_element("xpath", highlight_button_path)
highlight_button.click()
