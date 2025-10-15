

import requests

from datetime import datetime

res = requests.get("https://disease.sh/v3/covid-19/countries/Pakistan")

data = res.json()

# Convert Unix milliseconds to readable date
last_updated = datetime.fromtimestamp(data['updated'] / 1000).strftime('%Y-%m-%d %H:%M:%S')

print("🇵🇰 COVID-19 Stats for Pakistan")

print(f"🦠 Total Cases: {data['cases']} (+{data['todayCases']} today)")

print(f"❤️ Recovered: {data['recovered']} (+{data['todayRecovered']} today)")

print(f"💀 Deaths: {data['deaths']} (+{data['todayDeaths']} today)")

print(f"📊 Active Cases: {data['active']}")

print(f"😷 Critical Cases: {data['critical']}")

print(f"💉 Tests Conducted: {data['tests']}")

print(f"👥 Population: {data['population']}")

print(f"🗓️ Last Updated: {last_updated}")