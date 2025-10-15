import requests

zodiac_sign = "leo"
day = "today"

url = f"https://aztro.sameerkumar.website/?sign={zodiac_sign}&day={day}"
response = requests.post(url)

if response.status_code == 200:
    data = response.json()
    print(f"Horoscope for {zodiac_sign.capitalize()} ({day}):")
    print(data['description'])
    print("Mood:", data['mood'])
    print("Lucky number:", data['lucky_number'])
    print("Compatibility:", data['compatibility'])
else:
    print("Failed to fetch horoscope.")
