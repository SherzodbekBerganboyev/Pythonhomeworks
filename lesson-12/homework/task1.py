
from bs4 import BeautifulSoup

# HTML faylni ochish
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Ma'lumotlarni olish
forecast = []
rows = soup.find("tbody").find_all("tr")

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace("°C", ""))
    condition = cols[2].text.strip()
    forecast.append({
        "day": day,
        "temperature": temp,
        "condition": condition
    })

# Ma'lumotlarni chiqarish
print("5-Day Weather Forecast:")
for day_info in forecast:
    print(f"{day_info['day']}: {day_info['temperature']}°C, {day_info['condition']}")

# Eng issiq kun(lar)
max_temp = max(f["temperature"] for f in forecast)
hot_days = [f["day"] for f in forecast if f["temperature"] == max_temp]
print("\n🔥 Highest Temperature Day(s):", ", ".join(hot_days))

# Quyoshli kunlar
sunny_days = [f["day"] for f in forecast if f["condition"] == "Sunny"]
print("☀️ Sunny Day(s):", ", ".join(sunny_days))

# O‘rtacha harorat
avg_temp = sum(f["temperature"] for f in forecast) / len(forecast)
print(f"📈 Average Temperature: {avg_temp:.2f}°C")
