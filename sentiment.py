

import requests

comment="I Love severly the way this project turned out!"

base_url = "https://nocodefunctions.com/api/sentimentForAText"

params = {
    "text-lang": "en",
    "text": {comment},
    "explanation": "off",
    "output-format": "json",
    "explanation-lang": "en"
}

response = requests.get(base_url, params=params)

if response.status_code == 200:

    result = response.json()

    print("Mood:", result.get('sentiment'))

else:
    print("Error:", response.status_code)
