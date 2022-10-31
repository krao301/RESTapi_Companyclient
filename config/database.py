from pymongo import MongoClient


client = MongoClient("mongodb+srv://shravani:admin@cluster0.arl94pv.mongodb.net/?retryWrites=true&w=majority")

db = client.clientinfo_application

collection_name = db["clientinfo_app"]
