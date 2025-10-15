

import requests

res = requests.get("http://universities.hipolabs.com/search?country=Pakistan")

unis = res.json()

for idx, u in enumerate(unis[:5], start=1):

    print(f"\n{idx}. ")
    print(f"🏫 Name            : {u.get('name', 'N/A')}")

    print(f"🌍 Country         : {u.get('country', 'N/A')}")

    print(f"🇨🇴 Country Code   : {u.get('alpha_two_code', 'N/A')}")

    print(f"🗺️ State/Province : {u.get('state-province', 'Not Provided')}")

    domains = ", ".join(u.get('domains', []))

    web_pages = ", ".join(u.get('web_pages', []))

    print(f"🌐 Domains         : {domains}")

    print(f"🔗 Web Pages       : {web_pages}")