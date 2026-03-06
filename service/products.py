import json
from typing import List
from pathlib import Path

class ProductService:
    def __init__(self, data_file: str):
        self.data_file_path = Path(data_file)

    def get_all_products(self) -> List[dict]:
        if not self.data_file_path.exists():
            raise FileNotFoundError(f"Data file not found at {self.data_file_path}")
        
        with open(self.data_file_path, 'r') as file:
            products = json.load(file)
        return products

    def get_product_by_id(self, product_id: int) -> dict:
        products = self.get_all_products()
        for product in products:
            if product['id'] == product_id:
                return product
        return None