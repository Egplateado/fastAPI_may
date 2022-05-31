from typing import AnyStr
from fastapi import FastAPI, HTTPException
app = FastAPI()

items = {"foo" : "the foo wrestlers"}
#http://127.0.0.1:8000/
@app.get("items/{item_id}")
async def read_item(item_id:str):
    if iteem_id not in items:
        raise HTTPException(status_code=404 , detail = "Item not FOUND")
    else:
        print("Hello\n")
    return {"item" : items[item_id]}

 