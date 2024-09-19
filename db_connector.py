import psycopg2
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from config import MONGO_URI
from config import PG_DB_NAME, PG_USER, PG_PW, PG_HOST, PG_PORT


class MongodbConnector:

    def __init__(self):
        self.client = None
        self.create_mongodb_client()

    def create_mongodb_client(self):
        self.client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        self._check_connection()

    def _check_connection(self):
        try:
            self.client.admin.command('ping')
            print("Connected to MongoDB")
            return self.client
        except Exception as e:
            print("Error! Not connection to MongoDB")
            raise ConnectionError


class PostgresConnector:
    def __init__(self):
        self.connection = None
        self.create_postgres_connection()

    def create_postgres_connection(self):
        try:
            self.connection = psycopg2.connect(database=PG_DB_NAME,
                                               user=PG_USER,
                                               password=PG_PW,
                                               host=PG_HOST,
                                               port=PG_PORT)

            print("Connected to PostgreSQL")
            return self.connection
        except psycopg2.Error as error:
            print("Failed to connection ", error)
            return None

    def close_connection(self):
        self.connection.close()
        return None
