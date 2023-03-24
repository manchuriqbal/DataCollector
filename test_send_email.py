import smtplib


def send_email(email, height):

    sender = "Private Person <manchur.iqbal1@gmail.com>"
    receiver = "A Test User <email>"

    message = f"""\
    Subject: Hi Mailtrap
    To: {receiver}
    From: {sender}

    hey there your Height is <strong> %s <strong>. """ % height

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.login("823352b27b3b60", "7e1fd1e301c6c7")
        server.sendmail(sender, receiver, message)
