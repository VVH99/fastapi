from fastapi import FastAPI, Query, Path
from enum import Enum
from typing import Annotated
from pydantic import AfterValidator

app = FastAPI()

PRODUCTS = [
    {
        "id": 1,
        "title": "iPhone 15",
        "price": 999.99,
        "description": "Apple flagship smartphone with A16 Bionic chip"
    },
    {
        "id": 2,
        "title": "Samsung Galaxy S24",
        "price": 899.99,
        "description": "Premium Android smartphone with excellent camera"
    },
    {
        "id": 3,
        "title": "Google Pixel 8",
        "price": 699.99,
        "description": "Clean Android experience with AI-powered features"
    },
    {
        "id": 4,
        "title": "OnePlus 12",
        "price": 799.99,
        "description": "High-performance smartphone with fast charging"
    },
    {
        "id": 5,
        "title": "Nothing Phone 2",
        "price": 599.99,
        "description": "Unique design with Glyph interface and smooth performance"
    }

]


## Basic path validation

# @app.get("/products/{product_id}")
# async def get_product(product_id : int):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return { "error" : "Product Not found"}



# Numeric validation

# @app.get("/products/{product_id}")
# async def get_product(product_id : Annotated[int, Path(ge=1, le=5)]):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return {
#         "message" : "Product not found"
#     }

## Adding metadata

# @app.get("/products/{product_id}")
# async def get_product(product_id : Annotated[int, Path(le=1, ge=5 ,title = "Get products", description =" We can find products here")]):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return {
#         "error" : "Product not found"
#     }


## Path and query parameter combined

@app.get("/products/{product_id}")
async def get_products(product_id : Annotated[int, Path(ge=1, le=5)], search : Annotated[str | None, Query(max_length=20)] = None):
    for product in PRODUCTS:
        if product["id"] == product_id:
            if search and search.lower() not in product["title"].lower():
                return {
                    "error" : " THe search term doesn't match the products"
                }
            return product
    return {
        "error" : " Product not found"
    }
        



    
    