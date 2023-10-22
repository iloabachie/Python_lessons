import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import dotenv
import os

dotenv.load_dotenv("day32-email\.env")

smtp_server = os.getenv("YSERVER")
smtp_port = os.getenv("SMTP_PORT")
sender_email = os.getenv("YUSERNAME")
sender_password = os.getenv("YPASSWORD")

smtp_port = os.getenv("SMTP_PORT")
smtp_server = os.getenv("GSERVER")
sender_email = os.getenv("GUSERNAME")
sender_password = os.getenv("GPASSWORD")

recipient_emails = ["udemezue@gmail.com", "udemezue@outlook.com", "ezue1@yahoo.com"]

message = 'This message was sent from python using smtplib and email object'

msg = MIMEMultipart()
msg['To'] = ', '.join(recipient_emails)
msg['Cc'] = "udemezue@gs.com"
msg['Subject'] = 'A pythonic hello using the email object'
msg.attach(MIMEText(message, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    
    text = msg.as_string()
    print(text)
    # text = f'{subject}\n\n{message}'
    server.sendmail(sender_email, recipient_emails, text)
    
    print('Email sent successfully')

except Exception as e:
    print(f'Email could not be sent. Error: {str(e)}')

finally:
    server.quit()

