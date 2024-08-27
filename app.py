import random
import requests
import string
# A function to generate otp
def generateOTP():
    return ''.join(random.choices(string.digits, k=4))

def sendSMS(phone, otpcode):
    to = phone
    message = otpcode
    template_id = 'otp' #other templates: otp_1, welcome, welcome_1, reminder, reminder_, shopping, shopping_1, confirmation, confirmation_1
    server = 'https://sms.yegara.com/api2/send'
    username = 'domain-name' #use your own domain name and password
    password = 'password' 

        # Create the payload as a dictionary
    payload = {
        'username': username,
        'password': password,
        'to': to,
        'message': message,
        'template_id': template_id,
        }

     # Send a POST request to the server and get the response
    response = requests.post(server, json=payload)
    json_response = response.json()
    print(json_response)
