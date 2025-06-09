import requests

api_key = "6bc41ef7e6b144019fa91418250604"  # 👈 Replace with your actual key
city = input("Enter a city name: ")
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']
    print(f"\n🌍 Weather in {city}:\n🌡️ {temp}°C, 🌤️ {condition}")
else:
    print("❌ Failed to fetch weather. Check your city name or API key.")
