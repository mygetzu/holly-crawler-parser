from mongoengine import connect
from pymongo import MongoClient


class Database:
    host = "localhost"
    port = 27017
    client = None
    db = None
    topic = "hotel_reviews"

    def __init__(self):
        self.connect_mongo()

    def connect_mongo(self):
        try:
            self.client = MongoClient(host=self.host, port=self.port)
            self.db = self.client.hotel

            print("Success connecting to mongodb !\n")

        except:
            print("Failed to connect mongo database !\n")
