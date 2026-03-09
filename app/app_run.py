from email.policy import default
from pathlib import Path
from typing import Annotated
from fastapi import FastAPI, HTTPException, Query
from service.products import ProductService as ps

app = FastAPI()
product_service = ps(data_file="C:/Users/Dnyaneshwar.Shelke/Projects/fastapi-data-platform/data/products.json")

docs = """
Understanding FastAPI
FastAPI is a modern, fast (high-performance) web framework for building APIs with 
Python 3.6+ based on standard Python type hints. It is designed to be easy to use and to provide high performance, 
making it an excellent choice for building APIs quickly and efficiently.

Key Features of FastAPI
1. Fast: FastAPI is one of the fastest Python web frameworks available, thanks to its use of asynchronous programming and modern Python features.
2. Easy to Use: FastAPI is designed to be easy to use, 
with a simple and intuitive API that allows developers to quickly create APIs without needing to worry about the underlying details.
3. Type Hints: FastAPI uses Python's type hints to validate and serialize data, making it easier to catch errors early and ensuring that your API is well-documented.
4. Automatic Documentation: FastAPI automatically generates interactive API documentation using Swagger UI and ReDoc, making it easy for developers to understand and test your API.
5. Dependency Injection: FastAPI has built-in support for dependency injection, allowing you to manage your application's dependencies in a clean and efficient way.
6. Security: FastAPI provides built-in support for security features such as OAuth2, JWT, and HTTP Basic authentication, making it easier to secure your API.
7. Asynchronous Support: FastAPI supports asynchronous programming, allowing you to write non-blocking code that can handle a large number of requests efficiently.
8. Data Validation: FastAPI provides powerful data validation features, allowing you to define complex data models and validate incoming data against those models automatically.
9. Extensible: FastAPI is highly extensible, allowing you to add custom functionality and integrate with other libraries and frameworks as needed.
10. Community and Ecosystem: FastAPI has a growing community and a rich ecosystem of libraries and tools that can help you build your API more efficiently.
Overall, FastAPI is an excellent choice for building APIs in Python, offering a combination of speed, ease of use, and powerful features that can help you create robust and efficient APIs quickly and easily."""

@app.get("/")
async def read_root(params: dict = {
    "name": "dss"
}):
    return f"This is my first FASTAPI running on Localhost, {params['name']}!"

@app.get("/products/{item_id}")
async def read_item(item_id: int, query: str = None):
    products = ["This is item 1", "This is item 2"]
    return  products[item_id - 1] if item_id <= len(products) else HTTPException(status_code=404, detail="Item not found") 

@app.get("/products")
async def list_products(name: Annotated[str , Query(
                                    min_length = 1,
                                    max_length = 50,
                                    description = "The name of the product to retrieve")],
                        sorted_price: Annotated[bool, Query(
                                    description="Whether to sort products by price in descending order")],
                        orderby: Annotated[str, Query(
                                    description="The field to sort products by (e.g., 'price', 'name')")]="price"):
    
    products = product_service.get_all_products()
    print("products:", products)
    items = products.get('products', {}).get('data', {}).get('items', [])                      # type: list
    print("data:", items)

    if name:
        needle = name.strip().lower()
        p_name = [p for p in items if needle in p.get("name", "").lower()]

        if not p_name:
            raise HTTPException(404, f"Product with name '{name}' not found")
        return {"total_products": len(p_name), "products": p_name}
    
    if sorted_price:
        reverse = orderby.lower() == 'desc' 
        items = [p for p in items if isinstance(p.get("price"), (str, float))]
        items = sorted(filter(items, key=lambda x: float(x.get("price", 0)) if isinstance(x.get("price"), str) else x.get("price"), reverse=reverse))
        print("sorted_items:", items)

    return {"total_products": len(items), "products": items}

    

    