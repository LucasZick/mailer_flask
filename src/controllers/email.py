from src.controllers.message import MessageController
from src.models.message import MessageModel
from src import config
import smtplib
import ssl


class EmailController:
    
    @staticmethod
    def send_message(message_data):
        message_info = MessageModel(name=message_data['name'], email=message_data['email'], message=message_data['message'], language=message_data['language'])
        smtp_server = config.EMAIL['SMTP_SERVER']
        port = config.EMAIL['PORT']
        sender_email = config.MESSAGE['SENDER_EMAIL']
        owner_email = config.MESSAGE['OWNER_EMAIL']
        password = config.MESSAGE['PASSWORD']
        context = ssl.create_default_context()
        try:
            if config.DEBUG:
                print('Connecting to the server and starting sending')
            server = EmailController.connect(sender_email, password, smtp_server, port, context)
            message_owner = MessageController.generate_message_owner(sender_email, message_info)
            message_contactant = MessageController.generate_message_contactant(sender_email, message_info)
            server.sendmail(sender_email, owner_email, message_owner)
            if config.DEBUG:
                print(f"Notified {owner_email} about this message")
            server.sendmail(sender_email, message_info.email, message_contactant)
            if config.DEBUG:
                print(f"{message_info.name} was notified that you received his message")

        except Exception as err:
            print(f'Job function failure: {err}')
        finally:
            if config.DEBUG:
                print('Disconnecting from the server and finishing sending')
            server.quit()

    @staticmethod
    def connect(email, password, smtp_server, port, context):
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(email, password)
            if config.DEBUG:
                print('Server connected')
            return server
        except Exception as err:
            print(f'Connect function failure: {err}')
