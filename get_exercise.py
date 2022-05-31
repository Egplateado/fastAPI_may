import imp
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name" : "JOE"}, {"item_name" : "JOEL"} , {"item_name" : "OMAR"}]
#http://127.0.0.1:8000/lineas/?skip=0&limit=9
@app.get("/lineas/")
def read_item(skip: int = 0, limit: int = 9):
    return fake_items_db[skip: skip + limit]
#http://127.0.0.1:8000/items/4r/35
@app.get("/items/{item_id}/{needy}")
def read_user(item_id:str , needy:str , skip:int = 0 , limit:Optional[int] = None):
    item = {"item_id":item_id , "needy":needy , "skip":limit}
    return item