from unittest import TestCase
from src.nexus_api.email_alerts import EmailAlerts

class TestEmailAlerts(TestCase):

    def test_send_email(self):
        smtp_address = 'outlook.office365.com'
        smtp_port = 587

        # datos de la cuenta de envio
        sender_email_address = "no_reply@nexusintegra.io"
        email_password = 'Lok83000'

        # correo destinatario
        receiver_email_address = "operations@nexusintegra.io"
        E_Alerts = EmailAlerts(smtp_address, smtp_port, sender_email_address, email_password, receiver_email_address)
        subject = 'Test email alert - quicktask34'
        body = 'Tranquilos soy Ricardo haciendo pruebas'
        E_Alerts.send_email(subject, body)
        self.assertTrue(True)

    def test_email_alert_wrapper(self):
        self.fail()
