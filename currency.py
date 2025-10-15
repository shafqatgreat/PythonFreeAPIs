

import requests

base = "USD"

target = "EUR"

amount = 1

url = f"https://api.frankfurter.app/latest?amount={amount}&from={base}&to={target}"

response = requests.get(url)

data = response.json()

rate = data["rates"][target]

print(f"{amount} {base} = {rate} {target}")
