import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
     bot_token = os.environ.get("BOT_TOKEN")
     sql_url = os.environ.get("SQL_URL")
     webhook_domain = os.environ.get("WEBHOOK_DOMAIN")
     secret_webhook_token = os.environ.get("SECRET_WEBHOOK_TOKEN")
     logging_format = os.environ.get("LOGGING_FORMAT")
     alert_chat = os.environ.get("ALERT_CHAT")
     