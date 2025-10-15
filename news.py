

import requests

import pandas as pd

from io import StringIO

import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

query = 'technology sourcecountry:PK'

url = f'http://api.gdeltproject.org/api/v2/doc/doc?query={query}&mode=ArtList&format=CSV&maxrecords=5'

time.sleep(5)  # Wait for rate limit compliance

response = requests.get(url, headers=headers)

if response.status_code == 200 and response.text.strip() and 'limit requests' not in response.text:
    print("🔍 Response Preview:")

    print(response.text[:500])  # Peek at first few rows

    df = pd.read_csv(StringIO(response.text))

    print("\n🧠 Columns Returned:")

    print(df.columns.tolist())

    # Use safe column access and check for column existence

    for index, row in df.iterrows():
        title = row.get('Title', '[No Title]')
        link = row.get('URL', '[No Link]')

        print(f"📰 {title}")
        print(f"🔗 {link}")
        print("-" * 60)


else:

    print("⚠️ API response invalid or too frequent. Try again later.")