import smtplib
from email.message import EmailMessage
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")  

# send mail
def send_mail(data):
    email = EmailMessage()
    email['from'] = f'From my Portfolio'
    email['to'] = 'afeezdev@gmail.com'
    email['subject'] = data["subject"]
    
    email.set_content(f'From: {data["email"] } \n {data["message"]}')
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('afeezdev@gmail.com', PASSWORD)
        smtp.send_message(email)

# send sms 
def send_sms(data):
    account_sid = 'AC4235167a2f7e0e3c6c37de777052162b'
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+447481345912',
        body= f'From: {data["email"]} \nSubject: {data["subject"]} \n{data["message"]} ',
        to='+447852146308'
        )