
import requests

def send_sms(phone_number: str, message: str):

    response = requests.post('https://textbelt.com/text', {
    'phone': '+2348153353131',     # Use correct Pakistan number format
    'message': 'Hello from CodingMavrick!',
    'key': 'textbelt',            # Free key 
    })
    
    result = response.json()
    
    if result.get("success"):
            print("✅ SMS sent successfully.")
    else:
        print("❌ Failed to send SMS.")
        


if __name__ == "__main__":
    
    # Replace with a valid Pakistani number (format: +923xxxxxxxxx)
    phone_number = "+923200880488"
    message = "Hello from Python using Textbelt!"

    print(f"Sending SMS to {phone_number}...")
    send_sms(phone_number, message)


