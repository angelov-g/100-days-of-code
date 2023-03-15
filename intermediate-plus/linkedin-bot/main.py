from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3499654924&f_AL=true" \
      "&f_WT=2&keywords=Python%20Developer&refresh=true"

USER_EMAIL = os.environ.get("EMAIL")
USER_PASSWORD = os.environ.get("PASSWORD")

driver = webdriver.Chrome()

driver.get(URL)

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# Wait for page load
sleep(3)

email_field = driver.find_element(By.NAME, "session_key")
email_field.send_keys(USER_EMAIL)

password_field = driver.find_element(By.NAME, "session_password")
password_field.send_keys(USER_PASSWORD)
password_field.send_keys(Keys.RETURN)

# Wait for page load
sleep(5)

