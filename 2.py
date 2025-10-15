import requests
from datetime import datetime, timezone
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    quake_count = len(data["features"])
    
    # Print the number of earthquakes
    print(f"Number of Earthquakes in the Past 24 Hours: {quake_count}")
    
    # Loop through each earthquake and print the details
    for eq in data["features"]:
        location = eq['properties']['place']
        magnitude = eq['properties']['mag']
        time = eq['properties']['time'] / 1000  # Convert from milliseconds to seconds
        # Convert the Unix timestamp to a human-readable format
        formatted_time = datetime.fromtimestamp(time, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"Location: {location}, Magnitude: {magnitude}, Time: {formatted_time}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
