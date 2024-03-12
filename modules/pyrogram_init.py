from pyrogram.methods.utilities.idle import idle
from pyrogram import Client
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class PyrogramInit():
    def __init__(self, 
                 PORT=getenv("PORT"), 
                 HOST=getenv("HOST"),
                 API_HASH=getenv("API_HASH"),
                 API_ID=getenv("API_ID"),
                 BOT_TOKEN=getenv("BOT_TOKEN"),):
        
        self.PORT = PORT
        self.HOST = HOST
        self.API_HASH = API_HASH
        self.API_ID = API_ID
        self.BOT_TOKEN = BOT_TOKEN
        self.app = Client(name='TelegramBot', api_hash=self.API_HASH, api_id=self.API_ID, bot_token=self.BOT_TOKEN)
        
        
    def iniciar_bot(self):
        self.app.start()
        print("BOT INICIADO")
        idle()

