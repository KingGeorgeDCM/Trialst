from os import environ 

class Config:
    API_ID = environ.get("API_ID", "24820086")
    API_HASH = environ.get("API_HASH", "b7e4faf1ae700228512313cbc9bf0274")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6740529138:AAG3hrXaHpTnB8TrdBli0ON0Ztqa3Wpx8I4") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://kingeorgekabaap:karthik38@cluster0.juc5iqt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1130243906').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
