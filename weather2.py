import requests

def get_coordinates(city_name):
    url = f"https://nominatim.openstreetmap.org/search"
    params = {'format': 'json', 'q': city_name}
    headers = {'User-Agent': 'weather-app/1.0'}
    
    response = requests.get(url, params=params, headers=headers)
    
    try:
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
        else:
            print("No data found for this city.")
            return None, None
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Response was:", response.text)
        return None, None

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return data.get("current_weather", {})

# --- Main Program ---
city = input("Enter city name: ")
lat, lon = get_coordinates(city)

if lat is not None:
    weather = get_weather(lat, lon)
    if weather:
        print(f"\nCurrent weather in {city.title()}:\n")
        for key, value in weather.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
    else:
        print("Weather data not available.")
else:
    print("City not found.")
