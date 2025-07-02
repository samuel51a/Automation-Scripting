import smtplib
import os
from email.message import EmailMessage

# Email configuration
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
TO_ADDRESS = 'recipient@example.com'
SUBJECT = 'Daily Automated Email'
BODY = 'This is your daily automated email with attachments.'

# List all files in the current directory to attach
attachments = [f for f in os.listdir('.') if os.path.isfile(f)]

msg = EmailMessage()
msg['From'] = EMAIL_ADDRESS
msg['To'] = TO_ADDRESS
msg['Subject'] = SUBJECT
msg.set_content(BODY)

# Attach files
for file in attachments:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# Send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Change SMTP server and port if needed
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print("Email sent successfully!")