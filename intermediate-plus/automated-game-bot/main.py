from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/?_encoding=UTF8&pd_rd_w=zdMoy&"
#            "content-id=amzn1.sym.5724bc92-619d-4597-ac96-996c3c19e6c4&pf_rd_"
#            "p=5724bc92-619d-4597-ac96-996c3c19e6c4&pf_rd_r=CPRB15EHRJAA65P6QPBJ&pd_rd_"
#            "wg=kGxpL&pd_rd_r=8207332b-37ba-4a76-a84d-676d32fa93d6&ref_=pd_gw_ci_mcx_mr_hp_atf_m")
#
# price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"${price_whole.text}.{price_fraction.text}")

driver.get("https://www.python.org")

# go_button = driver.find_element(By.ID, "submit")
# print(go_button.size)

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# diversity_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[2]/a')
# print(diversity_link.text)

event_dict = {}
events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

for i in range(5):
    event_dict[i] = {"time": events[i].text.split("\n")[0], "name": events[i].text.split("\n")[1]}

# Angela's Solution
# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# for loop method
# for n in range(len(event_times)):
#     event_dict[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }

# dictionary comprehension
# event_dict = {n: {"time": event_times[n].text, "name": event_names[n].text} for n in range(len(event_times))}

print(event_dict)
