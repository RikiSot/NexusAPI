import smtplib, ssl
from email.message import EmailMessage
import os

class EmailAlerts:
    def __init__(self, email_address, email_port, email_sender, email_password, email_receiver):
        self.email_address = email_address
        self.email_password = email_password
        #self.email_server = email_server
        self.email_port = email_port
        self.email_sender = email_sender
        self.email_receiver = email_receiver

    def send_email(self, subject, body):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.email_sender
        msg['To'] = self.email_receiver
        msg.set_content(body)

        with smtplib.SMTP(self.email_address, self.email_port) as smtp:
            smtp.starttls(context=ssl.create_default_context())
            smtp.ehlo()
            smtp.login(self.email_address, self.email_password)
            smtp.send_message(msg)
            print("Email sent successfully")

    def email_alert_wrapper(self, fnc):
        def wrapper(*args, **kwargs):
            try:
                return fnc(*args, **kwargs)
            except Exception as e:
                print(e)
                subject = "EMAIL ALERT: ERROR IN: " + os.path.abspath(__file__)
                body = "ERROR: " + str(e) + "\n" + "FILE: " + os.path.abspath(__file__)
                self.send_email(subject, body)
        return wrapper
