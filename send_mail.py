import smtplib
from email.message import EmailMessage

import os  

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
        smtp.login('afeezdev@gmail.com', 'zpgzrqaxstylcagq')
        smtp.send_message(email)

