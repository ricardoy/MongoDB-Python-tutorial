from pymongo import MongoClient


class Persistence():
    def __init__(self, host='127.0.0.1', port=27017, user='', password='', db='', table=''):
        self.client = MongoClient(host=host, port=port)
        self.client.admin.authenticate(user, password)

        self.db = self.client[db]
        self.data = self.db[table]

    def insert(self, json_data):
        self.data.insert_one(json_data)

    def find_all_iterator(self):
        cursor = self.data.find({})
        return cursor
