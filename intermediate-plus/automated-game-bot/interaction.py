from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)

# content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# content_portals.click()

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys(Keys.RETURN)


sleep(2)

