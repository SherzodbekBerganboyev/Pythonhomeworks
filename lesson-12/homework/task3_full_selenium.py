
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import json

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

driver.get("https://www.demoblaze.com/index.html")

# Laptops bo'limiga o'tish
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Laptops").click()
time.sleep(3)

laptops = []

while True:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all("div", class_="card h-100")
    for item in items:
        name = item.find("a", class_="hrefch").text.strip()
        price = item.find("h5").text.strip()
        desc = item.find("p").text.strip()
        laptops.append({
            "name": name,
            "price": price,
            "description": desc
        })

    # "Next" tugmasi borligini tekshirish
    try:
        next_btn = driver.find_element(By.ID, "next2")
        if "disabled" in next_btn.get_attribute("class"):
            break
        next_btn.click()
        time.sleep(2)
    except:
        break

driver.quit()

# JSON formatda saqlash
with open("laptops_full.json", "w", encoding="utf-8") as f:
    json.dump(laptops, f, indent=4, ensure_ascii=False)

print("💾 All laptops saved to laptops_full.json")
