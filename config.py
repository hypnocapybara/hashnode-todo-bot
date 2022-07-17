import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    DATABASE_CONNECTION: str
    TELEGRAM_BOT_TOKEN: str


settings = Settings(
    DATABASE_CONNECTION=os.getenv('DATABASE_CONNECTION'),
    TELEGRAM_BOT_TOKEN=os.getenv('TELEGRAM_BOT_TOKEN'),
)
