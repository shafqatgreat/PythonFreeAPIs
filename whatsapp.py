#************************************
# Automating WhatsApp messages      *
#************************************
# First of all we will start with Scheduled message  
import pywhatkit  

# Send message to a contact at a scheduled time (hour, minute)  
# pywhatkit.sendwhatmsg('+923200880488', 'Hello from CodingMavrick!', 15, 30)  
# It will send Message on 3'Oclock and 30 minutes eg 03:30 hrs  

# Second Option is to send Message Instantly  
phone_number = '+923334519053'  
message = 'Welcome to CodingMavrick, your new go-to destination for all things programming!'   

# Method to Send immediately  

pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=15)  

#Open WhatsApp Web immediately  
#Wait 15 seconds to let page load  
#Send the message automatically

