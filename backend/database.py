from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@paa-chatbot.tp4urq2.mongodb.net/?retryWrites=true&w=majority")
db = client.flask_db
