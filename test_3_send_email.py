from email.mime.text import MIMEText
import smtplib


def send_email(email, height):
    from_email = "manchur.iqbal1@gmail.com"
    from_Pass = "bfaofmjrvltcpseu"
    to_email = email

    subject = "Height data"
    message = "hey there your Height is <strong> %s <strong>." % height

    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_Pass)
    gmail.send_message(msg)
