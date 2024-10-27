from pymongo import MongoClient
import pandas as pd  
class CRUD:
    def __init__(username,password):
        username = "aacuser"
        password = "jannatuldbuser"
        crud = CRUD(username, password)
        PORT = 31580
        DB = 'AAC'
        COL = 'animals'
        
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def read_all(self):
        """Retrieve all records from the database."""
        return list(self.collection.find())

    def filter_by_rescue_type(self, rescue_type):
        """Retrieve records based on the rescue type."""
        return list(self.collection.find({"rescue_type": rescue_type}))

    def filter_by_breed(self, breed):
        """Retrieve records based on the dog's breed."""
        return list(self.collection.find({"breed": breed}))

