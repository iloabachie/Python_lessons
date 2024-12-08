import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Email account credentials
outlook_email = "python.smtp@hotmail.com"
password = os.getenv("GPASSWORD")  # Use an app password if 2FA is enabled.

# Email details
recipient_email = "ezue1@yahoo.com"
subject = "Test Email from Python"
body = "Hello, this is a test email sent from Python using smtplib!"

# Create the email
message = MIMEMultipart()
message["From"] = outlook_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Connect to Outlook's SMTP server and send the email
try:
    # Use port 587 for TLS
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(outlook_email, password)  # Login to the server
        server.sendmail(outlook_email, recipient_email, message.as_string())  # Send the email
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
