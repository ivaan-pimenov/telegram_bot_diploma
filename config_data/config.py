import os
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    
    
@dataclass
class DB:
    host: str
    port: int
    user: str
    database: str
    password: str
    
    
@dataclass
class RapidApi:
    rapid_api_key: str
    max_hotel: int
    max_photo: int
    

@dataclass
class Config:
    tg_bot: TgBot
    db: DB
    rapid_api: RapidApi
    
    
def load_config() -> Config:
    """
    Load config form .env and return it
    :return: Config
    """
    if not os.getenv("BOT_TOKEN"):
        load_dotenv()
        
    return Config(
        tg_bot=TgBot(
            token=os.getenv("BOT_TOKEN"),
        ),
        db=DB(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            database=os.getenv("DB_NAME"),
            password=os.getenv("DB_PASS")
        ),
        rapid_api=RapidApi(
            rapid_api_key=os.getenv("RAPID_API_KEY"),
            max_hotel=int(os.getenv("MAX_HOTELS")),
            max_photo=int(os.getenv("MAX_PHOTOS"))
        ),
    )
