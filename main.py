from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app=FastAPI()
items =[]
class Item(BaseModel):
    name :str
    price: float
@app.post("/items")
def create_item(item:Item):
    items.append(item)
    return{"message":"item added","item":Item}
@app.get("/items",response_model=List[Item])
def get_items():
    return items