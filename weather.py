

import requests

cities = ["London", "New York", "Tokyo", "Karachi", "Sydney"]

for city in cities:
    response = requests.get(f"https://wttr.in/{city}?format=3")
    print(response.text)

