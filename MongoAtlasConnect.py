import pymongo


class MongoAtlasConnect:
    def __init__(self, data, db_name, table_name, username='ofir', password='ofir'):
        """

        :param data:
        :param db_name:
        :param table_name:
        :param username:
        :param password:
        """

        self.my_client = pymongo.MongoClient("mongodb+srv://{}:{}@cluster0-n0goo.gcp.mongodb.net/<dbname>?retryWrites"
                                             "=true&w=majority".format(username, password))
        self.database_name = self.my_client[db_name]
        self.my_collection = self.database_name[table_name]

        self.my_collection.insert_one(data)
        print('inserted into mongo')
