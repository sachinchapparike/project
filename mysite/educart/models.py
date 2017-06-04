'''from pymongo import MongoClient


class MongoConnection(object):

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client['mydatabase']
    def __str__(self):
	    return self.db

    def get_collection(self,people):
        self.collection = self.db['people']
        return self.collection'''