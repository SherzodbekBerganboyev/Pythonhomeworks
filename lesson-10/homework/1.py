import requests

API_KEY = "c590e426b0348a6cdb33b10dd2ecc95b"
CITY = "Tashkent"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    print(f"Ob-havo Tashkent shahrida:")
    print(f"🌡 Harorat: {temperature}°C")
    print(f"💧 Namlik: {humidity}%")
    print(f"🔎 Tavsif: {description.capitalize()}")
else:
    print("❌ Xatolik yuz berdi:", data.get("message", "Noma'lum xato"))
