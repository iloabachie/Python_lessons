import smtplib
from email.message import EmailMessage

# Step 1: Configure email details
sender_email = "your_email@example.com"
recipient_email = "recipient@example.com"
subject = "Automation Test Email"
body = "This is an automated email sent using Python."

# Step 2: Create email
msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject
msg.set_content(body)

# Step 3: Send email
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, "your_password")
    smtp.send_message(msg)