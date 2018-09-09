import os

from pymongo import MongoClient


def get_mongo_client(collection_name):
    client = MongoClient('mongodb://{}:{}@{}:{}/{}?authSource={}'.format(
        os.getenv('MONGO_USER'),
        os.getenv('MONGO_PASSWORD'),
        os.getenv('MONGO_HOST'),
        os.getenv('MONGO_PORT'),
        os.getenv('MONGO_DB'),
        os.getenv('MONGO_DB_AUTH')
    ))
    return client[os.getenv('MONGO_DB')][collection_name]
