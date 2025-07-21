from fastapi import APIRouter, Query, HTTPException
from models.product import ProductModel
from database import db
from bson import ObjectId
import re

router = APIRouter()

# Create a product
@router.post("/products", status_code=201)
def create_product(product: ProductModel):
    result = db.products.insert_one(product.dict())
    return {"message": "Product created", "id": str(result.inserted_id)}

# List products with optional filters
@router.get("/products", status_code=200)
def list_products(
    name: str = Query(None),
    size: str = Query(None),
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": re.escape(name), "$options": "i"}
    if size:
        query["size"] = size

    products = db.products.find(query).skip(offset).limit(limit)

    result = []
    for p in products:
        p["id"] = str(p["_id"])
        del p["_id"]
        result.append(p)

    return result

# Get product by ID
@router.get("/products/{product_id}", status_code=200)
def get_product_by_id(product_id: str):
    try:
        product = db.products.find_one({"_id": ObjectId(product_id)})
    except:
        raise HTTPException(status_code=400, detail="Invalid Product ID format")
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product["id"] = str(product["_id"])
    del product["_id"]
    return product

# Get products by name
@router.get("/products/search/by-name", status_code=200)
def get_products_by_name(name: str = Query(...)):
    products = db.products.find({"name": {"$regex": re.escape(name), "$options": "i"}})
    result = []
    for p in products:
        p["id"] = str(p["_id"])
        del p["_id"]
        result.append(p)
    return result

# Delete a product by ID
@router.delete("/products/{product_id}", status_code=200)
def delete_product(product_id: str):
    try:
        result = db.products.delete_one({"_id": ObjectId(product_id)})
    except:
        raise HTTPException(status_code=400, detail="Invalid Product ID format")
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}

# Delete all products
@router.delete("/products", status_code=200)
def delete_all_products():
    db.products.delete_many({})
    return {"message": "All products deleted"}
