import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pokemon-battle-secret-key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://mongo:27017/pokemon'
