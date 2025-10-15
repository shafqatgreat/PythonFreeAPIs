import requests


# Indicator Name	Code
# Malaria Incidence	MALARIA_CASES
# HIV Estimates	HIV_0000000001
# Measles Reported Cases	MEASLES_REPORTED
# Polio Reported Cases	POLIO_REPORTED
# Hepatitis B Prevalence	HEPB_PREVALENCE


# Example indicator (you'll replace with a real one from previous step)
indicator_code = "MALARIA_CASES"  # Hypothetical malaria indicator

url = f"https://ghoapi.azureedge.net/api/{indicator_code}"
response = requests.get(url)

if response.ok:
    malaria_data = response.json()['value']

    # Filter for Congo data
    pak_data = [entry for entry in malaria_data if 'PAK' in entry['SpatialDim'].upper()]
    # Sort by year (TimeDim) ascending
    pakistan_data_sorted = sorted(pak_data, key=lambda x: x.get('TimeDim', 0), reverse=True)

    for entry in pakistan_data_sorted[:10]:
        print(f"🌍 Country: {entry['SpatialDim']} | Year: {entry['TimeDim']} | Cases Reported: {entry['Value']}")
else:
    print("❌ Failed to fetch data.")
