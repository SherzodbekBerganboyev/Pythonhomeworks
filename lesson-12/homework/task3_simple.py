
import requests
from bs4 import BeautifulSoup
import json

base_url = "https://www.demoblaze.com/index.html"

def get_laptops_from_page(soup):
    laptops = []
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
    return laptops

response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

laptop_data = get_laptops_from_page(soup)

with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptop_data, f, indent=4, ensure_ascii=False)

print("💾 Laptops saved to laptops.json")
