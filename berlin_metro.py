


import requests

res = requests.get("https://v5.vbb.transport.rest/locations?query=Berlin&type=station")

stations = res.json()

for s in stations[:10]:  # Just showing 10 stations
    
    print(f"Station: {s['name']}")

    print(f"ID: {s['id']}")

    print(f"Coordinates: ({s['location']['latitude']}, {s['location']['longitude']})")

    print("Supports:")

    # Dictionary [('suburban', False), ('subway', False)]

    for k, v in s['products'].items():
        if v:
            print(f"  ✅ {k}")

    print("-" * 40)
