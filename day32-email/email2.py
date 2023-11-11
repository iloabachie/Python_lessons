import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from loremipsum import get_paragraph
from icecream import ic
import dotenv
import os

dotenv.load_dotenv("day32-email\.env")

smtp_port = os.getenv("SMTP_PORT")
smtp_server = os.getenv("GSERVER")
sender_email = os.getenv("GUSERNAME")
sender_password = os.getenv("GPASSWORD")
ic(smtp_port, smtp_server, sender_email, sender_password)

recipient_emails = ["udemezue@gmail.com", "udemezue@outlook.com"]
# recipient_emails = ["info@anchorlimited.net", "ropsvq@hldrive.com", 'wellensteinkristine879@gmail.com']

message =  get_paragraph()

msg = MIMEMultipart()
msg['From'] = "The FBI WatchDog"
msg['To'] = ', '.join(recipient_emails)
msg['Cc'] = "ezue1@yahoo.com"
msg['Subject'] = 'Continue the Scams Till You get Caught'
msg.attach(MIMEText(message, 'plain'))

# attach image
with open('day32-email\Image.jpg', 'rb') as img_file:
    image = MIMEImage(img_file.read(), name="watching you.jpg")
msg.attach(image)

# attach pdf
with open('day32-email\okoro.pdf', 'rb') as pdf_file:
    pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
    pdf_attachment.add_header('content-disposition', 'attachment', filename='be warned.pdf')
msg.attach(pdf_attachment)


try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    
    text = msg.as_string()
    # print(text)
    server.sendmail(sender_email, recipient_emails, text)
    
    print('Email sent successfully')

except Exception as e:
    print(f'Email could not be sent. Error: {str(e)}')

finally:
    server.quit()

