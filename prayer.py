

import requests

city = "Karachi"

country = "Pakistan"

url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"

data = requests.get(url).json()

timings = data['data']['timings']

for key, time in timings.items():
    print(f"{key}: {time}")
