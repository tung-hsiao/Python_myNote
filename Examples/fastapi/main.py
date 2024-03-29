from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create an instance of the FastAPI class
app = FastAPI()

# Define a Pydantic model for request body validation
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Dummy database to store items
fake_items_db = []

# POST API endpoint to create a new item
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    fake_items_db.append(item_dict)
    return item_dict


'''
You can test this server using tools like cURL, Postman, or any other HTTP client. Here's an example cURL command to create a new item:
curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"name":"New Item","description":"A new item","price":10.5,"tax":1.5}'
'''