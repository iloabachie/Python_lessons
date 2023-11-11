import smtplib
import dotenv
import os
from loremipsum import get_paragraph
from icecream import ic

dotenv.load_dotenv("day32-email\.env")

# Set up the connection to the SMTP server
smtp_port = os.getenv('SMTP_PORT')
smtp_server = os.getenv("GSERVER")
smtp_username = os.getenv("GUSERNAME")
smtp_password = os.getenv("GPASSWORD")

ic(smtp_server, smtp_username, smtp_port, smtp_password)

# Create a secure connection to the SMTP server
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)

smtp_connection.starttls()

# Log in to your Gmail account
smtp_connection.login(smtp_username, smtp_password)

# Send an email
from_address = smtp_username

# to_address = "udemezue@gmail.com"
to_address = ["udemezue@gmail.com", "udemezue@outlook.com", "ezue1@yahoo.com"]
# to_address = ["info@anchorlimited.net", "ropsvq@hldrive.com", 'wellensteinkristine879@gmail.com']

subject = "Hello Scammers You will be caught soon its a matter of time"

body = get_paragraph()

message = f"To: abc@def.com\nCc: efg@hij.com\nSubject: {subject}\n{body}"

for _ in range(10):
    smtp_connection.sendmail(from_address, to_address, message)

# Close the connection
smtp_connection.quit()

