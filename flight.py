import requests

# Input flight number (callsign)
flight_number = input("Enter flight number (callsign): ").strip().upper()

# Fetch data from OpenSky API
url = "https://opensky-network.org/api/states/all"
response = requests.get(url, timeout=10)

if response.status_code == 200:
    data = response.json()
    states = data.get('states', [])

    found = False

    for flight in states:
        callsign = flight[1].strip() if flight[1] else ""
        if callsign.upper() == flight_number:
            print(f"\n✈️ Flight Found: {callsign}")
            print(f"  ICAO 24bit Address: {flight[0]}")
            print(f"  Origin Country: {flight[2]}")
            print(f"  Time Position: {flight[3]}")
            print(f"  Last Contact: {flight[4]}")
            print(f"  Longitude: {flight[5]}")
            print(f"  Latitude: {flight[6]}")
            print(f"  Baro Altitude: {flight[7]}")
            print(f"  On Ground: {flight[8]}")
            print(f"  Velocity (m/s): {flight[9]}")
            found = True
            break

    if not found:
        print(f"No data found for flight number '{flight_number}'.")
else:
    print(f"Error fetching data: {response.status_code}")




# [
#   "4b1816",      // [0] ICAO 24-bit address
#   "SWR87C  ",    // [1] ✅ Callsign (this is the flight number)
#   "Switzerland", // [2] Origin Country
#   1744888078,    // [3] Time Position (Unix timestamp)
#   1744888085,    // [4] Last Contact (Unix timestamp)
#   8.5564,        // [5] Longitude
#   47.4527,       // [6] Latitude
#   480.06,        // [7] Barometric Altitude
#   true,          // [8] On Ground
#   0.06,          // [9] Velocity
#   334.69,        // [10] Heading (true track)
#   null,          // [11] Vertical rate
#   null,          // [12] Sensors
#   null,          // [13] Geo altitude
#   "1000",        // [14] Squawk
#   false,         // [15] SPI
#   0              // [16] Position source
# ]
