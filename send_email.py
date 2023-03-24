import ssl
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage


def send_email(email, height, height_avg, count):
    from_email = "manchur.fiverr@gmail.com"
    from_Pass = "xsnukxppwwjrfugz"
    to_email = email

    subject = "Height data"
    message = "hey there your Height is %s. avarage height of all is %s and that is calculate out of %s pepole." % (
        height, height_avg, count)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email
    msg.set_content(message)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(from_email, from_Pass)
        smtp.sendmail(from_email, to_email, msg.as_string())
