import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
BATCH_DB = os.getenv('BATCH_DB')
ORDERS_COLL = os.getenv('ORDERS_COLL')
VISITS_COLL = os.getenv('VISITS_COLL')

PG_DB_NAME = os.getenv('PG_DB_NAME')
PG_USER = os.getenv('PG_USER')
PG_PW = os.getenv('PG_PW')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')