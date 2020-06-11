import pymongo


class MongoAtlasConnect:
    """
    connects to MongoDB Atlas.
    checks if item exists in the DB, if not then insert it. if it dose exists then it will update the metadata.
    """
    def __init__(self, data, db_name, table_name):
        address_to_mongo = ""

        self.data = data
        self.my_client = pymongo.MongoClient(address_to_mongo)
        self.database_name = self.my_client[db_name]
        self.my_collection = self.database_name[table_name]

    def dose_item_exists(self):
        item_exists = self.my_collection.find_one({"file name": self.data['file name']})

        if item_exists is not None:
            self.update_metadata(item_exists['_id'])
        else:
            self.insert_metadata()

    def update_metadata(self, obj_id):
        self.my_collection.update_one({'_id': obj_id}, {"$set": {'metadata': self.data['metadata']}})
        print('metadata updated in mongo')

    def insert_metadata(self):
        self.my_collection.insert_one(self.data)
        print('inserted into mongo')
