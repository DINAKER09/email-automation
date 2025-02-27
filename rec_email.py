import smtplib
from email.message import EmailMessage

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient_email

        # Using SMTP_SSL on port 465:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Replace with your details
sender_email = "dinakerreddy6@gmail.com"
app_password = "xthuocpnienudqlz"  # Use an app password if 2FA is enabled
recipient_email = "dinakerreddykesireddy@gmail.com"
subject = "Test Email"
body = "This is a test email sent from a Python script.2"


send_email(sender_email, app_password, recipient_email, subject, body)
