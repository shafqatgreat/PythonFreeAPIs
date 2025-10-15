


import requests

country = "US"
year = 2025

url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country}"

holidays = requests.get(url).json()

for h in holidays:
    print(h['date'], '-', h['localName'])
