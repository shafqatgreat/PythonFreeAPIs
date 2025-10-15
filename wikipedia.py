import requests

topic = "Artificial_intelligence"
url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("📘 Title:", data.get("title", "N/A"))
    print("📄 Description:", data.get("description", "N/A"))
    print("📝 Summary:\n", data.get("extract", "N/A"))
    print("🔗 URL:", data.get("content_urls", {}).get("desktop", {}).get("page", "N/A"))

    thumbnail = data.get("thumbnail", {})
    if thumbnail:
        print("🖼️ Image URL:", thumbnail.get("source", "No image"))
        print("📐 Image Dimensions:", f"{thumbnail.get('width')}x{thumbnail.get('height')}")
    
    print("📦 Page Length:", data.get("length", "N/A"))
    print("📅 Last Updated:", data.get("timestamp", "N/A"))
else:
    print("❌ Failed to fetch summary:", response.status_code)
