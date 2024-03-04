from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src import config


class MessageController:

    @staticmethod
    def generate_message_owner(sender_email, message_info):
        html = MessageController.generate_html_owner(message_info)
        message = MIMEMultipart("alternative", None, [MIMEText(html, 'html')])
        message["From"] = sender_email
        message["To"] = ','.join(config.MESSAGE['OWNER_EMAIL'].split(','))
        message["Subject"] = f"You have a new message from {message_info.name}"
        message.attach(MIMEText(html, "html"))
        msg_body = message.as_string()
        if config.DEBUG:
            print('Message generated for owner')
        return msg_body
    
    @staticmethod
    def generate_message_contactant(sender_email, message_info):
        if message_info.language == "pt":
            subject = f"Olá {message_info.name}! Recebi o seu contato"
        elif message_info.language == "de":
            subject = f"Hallo {message_info.name}! ich habe deine Kontaktaufnahme erhalten!"
        else:
            subject = f"Hello {message_info.name}! I received your contact"

        html = MessageController.generate_html_contactant(message_info)
        message = MIMEMultipart("alternative", None, [MIMEText(html, 'html')])
        message["From"] = sender_email
        message["To"] = message_info.email
        message["Subject"] = subject
        message.attach(MIMEText(html, "html"))
        msg_body = message.as_string()
        if config.DEBUG:
            print('Message generated for contactant')
        return msg_body
    
    @staticmethod
    def generate_html_contactant(message_info):
        language = message_info.language
        if language == 'pt':
            greeting = 'Olá'
            confirmation_message = 'Confirmação de Mensagem Recebida'
            thank_you_message = 'Obrigado por entrar em contato. Abaixo estão as informações que você enviou:'
            contact_message = 'Se tudo estiver correto, você não precisa fazer mais nada. Caso note alguma inconsistência ou queira fornecer mais informações, por favor, entre em contato diretamente respondendo a este email.'
            closing_message = 'Agradeço pela sua mensagem! Em breve, entrarei em contato para fornecer uma resposta.'
            name, email, message = "Nome", "Email", "Mensagem"
        elif language == 'de':
            greeting = 'Hallo'
            confirmation_message = 'Bestätigung der erhaltenen Nachricht'
            thank_you_message = 'Danke für Ihre Kontaktaufnahme. Hier sind die Informationen, die Sie bereitgestellt haben:'
            contact_message = 'Wenn alles korrekt ist, müssen Sie nichts weiter tun. Wenn Ihnen Unstimmigkeiten auffallen oder Sie weitere Informationen bereitstellen möchten, wenden Sie sich bitte direkt an uns, indem Sie auf diese E-Mail antworten.'
            closing_message = 'Danke für deine Nachricht! Ich werde mich bald mit einer Antwort bei Ihnen melden.'
            name, email, message = "Name", "Email", "Nachricht"
        else:
            greeting = 'Hello'
            confirmation_message = 'Confirmation of Received Message'
            thank_you_message = 'Thank you for reaching out. Below are the details you provided:'
            contact_message = 'If everything is correct, you don\'t need to do anything else. If you notice any inconsistency or want to provide more information, please contact directly by replying to this email.'
            closing_message = 'Thank you for your message! I will get back to you soon with a response.'
            name, email, message = "Name", "Email", "Message"
        html_template = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    background-color: #f8f8f8;
                }}
                .message-box {{
                    margin-top: 20px;
                    padding: 10px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    background-color: #fff;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>{confirmation_message}</h2>
                <p>{greeting} {message_info.name},</p>
                <p>{thank_you_message}</p>
                <div class="message-box">
                    <p><strong>{name}:</strong> {message_info.name}</p>
                    <p><strong>{email}:</strong> {message_info.email}</p>
                    <p><strong>{message}:</strong> {message_info.message}</p>
                </div>
                <p>{contact_message}</p>
                <p>{closing_message}</p>
            </div>
        </body>
        </html>
        """

        return html_template
    
    @staticmethod
    def generate_html_owner(message_info):
        html_template = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    background-color: #f8f8f8;
                }}
                .message-box {{
                    margin-top: 20px;
                    padding: 10px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    background-color: #fff;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>New contact request received!</h2>
                <p><strong>{message_info.name}</strong> sent a message.</p>
                <p><strong>{message_info.name}{'' if message_info.name[-1].upper() == "S" else "'s"}</strong> email is: {message_info.email}</p>
                <div class="message-box">
                    <p><strong>Message:</strong></p>
                    <p>{message_info.message}</p>
                </div>
            </div>
        </body>
        </html>
        """

        return html_template