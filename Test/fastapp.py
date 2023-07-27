from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
client = MongoClient('mongodb://localhost:27017/')
db = client['EntityDB']
collection = db['entityCollection']


@app.get('/list')
def list_items(item_id: int):
    document = collection.find()
    return document




