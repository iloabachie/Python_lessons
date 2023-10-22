import smtplib
import dotenv
import os

dotenv.load_dotenv("day32-email\.env")

# Set up the connection to the SMTP server
smtp_port = os.getenv("SMTP_PORT")
smtp_server = os.getenv("GSERVER")
smtp_username = os.getenv("GUSERNAME")
smtp_password = os.getenv("GPASSWORD")

# Create a secure connection to the SMTP server
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)

smtp_connection.starttls()

# Log in to your Gmail account
smtp_connection.login(smtp_username, smtp_password)

# Send an email
from_address = smtp_username

# to_address = "udemezue@gmail.com"
to_address = ["udemezue@gmail.com", "udemezue@outlook.com", "ezue1@yahoo.com"]

subject = "Hello from google Python!"

body = "This is the body of the email where i test the fields entry"

message = f"To: abc@def.com\nCc: efg@hij.com\nSubject: {subject}\n{body}"

smtp_connection.sendmail(from_address, to_address, message)

# Close the connection
smtp_connection.quit()

# ======================================================================

smtp_port = os.getenv("SMTP_PORT")
smtp_server = os.getenv("YSERVER")
smtp_username = os.getenv("YUSERNAME")
smtp_password = os.getenv("YPASSWORD")

# Create a secure connection to the SMTP server
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)

smtp_connection.starttls()

# Log in to your Gmail account

smtp_connection.login(smtp_username, smtp_password)

# Send an email

from_address = smtp_username

addresses = ["udemezue@gmail.com", "udemezue@outlook.com", "ezue1@yahoo.com"]

subject = "Hello from Yahoo Python!"

body = "This is the body of the yahoo email server sent out email."

message = f"Subject: {subject}\n\n{body}"

for address in addresses:
    smtp_connection.sendmail(from_address, address, message)

# Close the connection
smtp_connection.quit()