from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from time import sleep
import os


def load_all_results():
    top_job = driver.find_element(By.CLASS_NAME, "job-card-list__title")
    top_job_link = driver.find_element(By.LINK_TEXT, top_job.text)
    top_job_link.click()

    while True:
        try:
            driver.find_element(By.LINK_TEXT, "About")
            break
        except NoSuchElementException:
            top_job_link.send_keys(Keys.PAGE_DOWN)


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

login = input()
# Wait for page load
sleep(4)

load_all_results()

jobs = driver.find_elements(By.CLASS_NAME, "job-card-list__title")
for job in jobs:
    job_title = job.text
    job_link = driver.find_element(By.LINK_TEXT, job_title)
    job_link.click()

    sleep(2)

    apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
    apply_button.click()

    sleep(2)

    submit_button = driver.find_element(By.CSS_SELECTOR, ".pv4 button")

    if submit_button.text != "Submit application":
        close_button = driver.find_element(By.CSS_SELECTOR, "button")
        close_button.click()
        discard_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar button")
        discard_button.click()

    else:
        phone_field = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
        phone_field.send_keys("123456789")

        resume_choose = driver.find_element(By.CSS_SELECTOR, ".jobs-resume-picker__resume-btn-container button")
        resume_choose.click()

        submit_button.click()

# UNFINISHED
