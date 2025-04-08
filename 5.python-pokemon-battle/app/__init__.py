from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Configure MongoDB
client = MongoClient(app.config['MONGO_URI'])
db = client.get_database()

from app.routes import api
app.register_blueprint(api.bp)
