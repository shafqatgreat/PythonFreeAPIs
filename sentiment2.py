import requests

# List of comments to analyze
comments = [
    "I love how clean the design is!",
    "This is the worst experience I've ever had.",
    "Not bad, could be better.",
    "Absolutely fantastic! Highly recommended.",
    "I hate severely the way this project turned out!",
    "Meh, it’s okay I guess.",
    "What a terrible mistake this was.",
    "Super excited about this release!",
    "I’m not sure what to think about this.",
    "It’s just perfect!"
]

# API endpoint
base_url = "https://nocodefunctions.com/api/sentimentForAText"

# Common parameters (can be changed if needed)
base_params = {
    "text-lang": "en",
    "explanation": "off",          # Set to 'on' if you want detailed explanations
    "output-format": "json",
    "explanation-lang": "en"
}

# Iterate over each comment
for i, comment in enumerate(comments, 1):
    params = base_params.copy()
    params["text"] = comment

    response = requests.get(base_url, params=params)

    print(f"\nComment #{i}: {comment}")
    if response.status_code == 200:
        result = response.json()
        print("  ➤ Mood:", result.get("sentiment", "Unknown"))
    else:
        print("  ✖ Error:", response.status_code)
