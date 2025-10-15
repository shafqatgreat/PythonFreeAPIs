import requests
import json

# Alpha Vantage demo API endpoint for intraday stock data (5min interval)
url = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "GOOGL",
    "interval": "5min",
    "apikey": "demo"
}

# Send GET request
response = requests.get(url, params=params)

# Parse response JSON
data = response.json()

# Extract time series data
time_series = data.get("Time Series (5min)", {})

if time_series:
    # Get the latest timestamp entry
    latest_time = sorted(time_series.keys())[-1]
    latest_data = time_series[latest_time]
    latest_price = latest_data.get("1. open")

    print(f"Latest stock price for GOOGL at {latest_time} is: ${latest_price}")
else:
    print("No data found or API limit reached.")
