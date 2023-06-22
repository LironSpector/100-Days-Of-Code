from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver_service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=driver_service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 5 * 60

while True:
    cookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(price.text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for i in range(len(item_prices)):
            cookie_upgrades[item_prices[i]] = items_ids[i]

        money = int(driver.find_element(By.ID, "money").text)

        affordable_upgrades = {}
        for price, id in cookie_upgrades.items():
            if money > price:
                affordable_upgrades[price] = id

        max_affordable_upgrade = max(affordable_upgrades, default=0)
        max_affordable_upgrade_id = affordable_upgrades[max_affordable_upgrade]

        driver.find_element(By.ID, max_affordable_upgrade_id).click()

        timeout += 5

    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, "cps").text
        print(cookie_per_sec)
        break

driver.quit()
