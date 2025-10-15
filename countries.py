

import requests

country = "Japan"

url = f"https://restcountries.com/v3.1/name/{country}"

data = requests.get(url).json()

info = data[0]

print("🏙️ Capital:", info['capital'][0])

print("👥 Population:", info['population'])

print("🌍 Area:", info['area'], "sq km")

print("💱 Currency:", list(info['currencies'].keys())[0])