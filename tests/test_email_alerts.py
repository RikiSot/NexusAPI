from unittest import TestCase
from src.nexus_api.email_alerts import EmailAlerts
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os

# Set test options and .env file

BASE_DIR = Path('..')
dotenv_path = BASE_DIR / 'secrets.env'
load_dotenv(find_dotenv(dotenv_path))


class TestEmailAlerts(TestCase):
    smtp_address = 'outlook.office365.com'
    smtp_port = 587

    # datos de la cuenta de envio
    sender_email_address = os.getenv("SENDER_EMAIL_ADDRESS")
    email_password = os.getenv("EMAIL_PASSWORD")
    receiver_email_address = os.getenv("RECEIVER_EMAIL_ADDRESS")

    subject = 'Test email alert'
    body = 'Prueba de envio de email mediante el SDK de Nexus'
    e_alerts = EmailAlerts(smtp_address, smtp_port, sender_email_address, email_password, receiver_email_address)

    def _test_send_email(self):
        self.e_alerts.send_email(self.subject, self.body)
        self.assertTrue(True)

    def test_email_alert_wrapper(self):
        e_alerts = EmailAlerts(self.smtp_address, self.smtp_port, self.sender_email_address, self.email_password,
                               self.receiver_email_address)

        # Set environment info for email alert to test
        e_alerts.set_email_alert_info(self.subject, self.body, environment='test')

        # If you want to test the email alert wrapper, you can uncomment the following lines
        @e_alerts.email_alert_wrapper
        def mock_function():
            raise Exception('Test exception')

        mock_function()
        self.assertTrue(True)
