import os
from twilio.rest import Client
import smtplib

MY_EMAIL = "lirontheprog@gmail.com"
MY_PASSWORD = "ciexaniegletpvnu"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    # def send_email(self):
    def send_sms(self, message_to_send):
        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=message_to_send,
            from_='+15617833092',
            to='+972 53 965 4065'
            )

    def send_email(self, message_to_send, email_to_send):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email_to_send,
                msg=message_to_send)

