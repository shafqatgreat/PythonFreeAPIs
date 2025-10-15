import requests
from datetime import datetime, timezone
# Define the API endpoint and parameters
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "geojson",
    "starttime": "2004-04-15",  # Example: 5 years ago from today
    "endtime": "2023-04-15",    # Example: today's date
    "minlatitude": 24.396308,   # Southern boundary of Pakistan
    "maxlatitude": 37.0841,     # Northern boundary of Pakistan
    "minlongitude": 65.951,     # Western boundary of Pakistan
    "maxlongitude": 73.0369,    # Eastern boundary of Pakistan
    "minmagnitude": 6.0,        # Optionally filter by magnitude
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    quake_count = len(data["features"])

    print(f"Number of Earthquakes in the Last 5 Years in Pakistan: {quake_count}")
    
    # Display earthquake details
    for eq in data["features"]:
        location = eq['properties']['place']
        magnitude = eq['properties']['mag']
        time = eq['properties']['time'] / 1000  # Convert from milliseconds to seconds
        formatted_time = datetime.fromtimestamp(time, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"Location: {location}, Magnitude: {magnitude}, Time: {formatted_time}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
