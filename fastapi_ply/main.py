from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    isoffer: bool = None

@app.get("/")
def read_root():
    return {"hello":"cash"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = 'just'):
    return {"item_id": item_id, "q": q}

@app.get("/stuff/{stuff_id}")
def read_stuff(stuff_id: int, p: str = None):
    return {"stuff_id": stuff_id, "p": p}

@app.get("/fx/{symbol}")
def read_fx(symbol: str, price: float):
    return {"symbol": symbol, "price": price/2}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": Item.price}