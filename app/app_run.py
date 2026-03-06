from os import name
from pathlib import Path
from fastapi import FastAPI, HTTPException
from service.products import ProductService as ps

app = FastAPI()
product_service = ps(data_file="C:/Users/Dnyaneshwar.Shelke/Projects/fastapi-data-platform/data/products.json")

@app.get("/")
async def read_root(params: dict = {
    "name": "dss"
}):
    return f"This is my first FASTAPI running on Localhost, {params['name']}!"

@app.get("/items/{item_id}")
async def read_item(item_id: int, query: str = None):
    items = ["This is item 1", "This is item 2"]
    return  items[item_id - 1] if item_id <= len(items) else HTTPException(status_code=404, detail="Item not found") 

@app.get("/products")
async def read_products():
    return product_service.get_all_products()

