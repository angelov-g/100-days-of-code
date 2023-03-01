from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_driver_path = "/selenium_driver/chromedriver"
driver = webdriver.Chrome()

driver.get("https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/?_encoding=UTF8&pd_rd_w=zdMoy&"
           "content-id=amzn1.sym.5724bc92-619d-4597-ac96-996c3c19e6c4&pf_rd_"
           "p=5724bc92-619d-4597-ac96-996c3c19e6c4&pf_rd_r=CPRB15EHRJAA65P6QPBJ&pd_rd_"
           "wg=kGxpL&pd_rd_r=8207332b-37ba-4a76-a84d-676d32fa93d6&ref_=pd_gw_ci_mcx_mr_hp_atf_m")

price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(f"${price_whole.text}.{price_fraction.text}")



