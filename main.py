from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory storage
items = []
db = {}

# Item model and endpoints
class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item added", "item": item}

@app.get("/items", response_model=List[Item])
def get_items():
    return items

# Activity model and endpoints
class Activity(BaseModel):
    id: int
    metric_name: str
    value: float

@app.put("/update/{item_id}")
def update_activity(item_id: int, activity: Activity):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    db[item_id] = {"metric_name": activity.metric_name, "value": activity.value}
    return {"message": "Activity updated", "data": db[item_id]}

@app.delete("/delete/{item_id}")
def delete_activity(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"message": f"Item with ID {item_id} deleted"}
