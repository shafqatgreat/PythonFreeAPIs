
import requests 
def send_sms(): 
    response = requests.post  
    ('https://textbelt.com/text',  
     { 
         'phone': '+923200880488',     # Use correct Pakistan number format 
         'message': 'Hello from CodingMavrick!', 
         'key': 'textbelt',            # Free key  

     })
    
    result = response 
    if result.get("success"): 
                print(" SMS sent successfully.") 
    else: 
                print(" Failed to send SMS.") 

if __name__ == "__main__": 
        # Call the function send_sms  
         
         send_sms() 
         