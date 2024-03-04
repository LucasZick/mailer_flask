from os import environ

DEBUG = environ.get('DEBUG', False)

EMAIL = {
    "SMTP_SERVER": environ.get("SMTP_SERVER", "smtp.gmail.com"),
    "PORT": environ.get("PORT", 587),
}

MESSAGE = {
    'SENDER_EMAIL': environ.get('SENDER_EMAIL'),
    'OWNER_EMAIL': environ.get('OWNER_EMAIL'),
    'PASSWORD': environ.get('PASSWORD')
}