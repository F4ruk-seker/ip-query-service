import pymongo
from bson.objectid import ObjectId
from datetime import datetime
import os


def save_query(data) -> dict:
    connection_key = os.getenv('MONGO_DB_CONNECTION')
    connection = pymongo.MongoClient(connection_key)
    com = connection['pars_ip_api']
    ip_list = com['ip_query_list']
    data['questioned_date'] = datetime.now()
    ip_list.insert_one(data)
    connection.close()
    data['_id'] = str(data['_id'])
    return data


def get_ip_from_id(_id):
    connection_key = os.getenv('MONGO_DB_CONNECTION')
    connection = pymongo.MongoClient(connection_key)
    try:
        com = connection['pars_ip_api']
        ip_list = com['ip_query_list']
        results = ip_list.find_one(ObjectId(_id))
        return results
    finally:
        connection.close()


