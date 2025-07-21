from fastapi import FastAPI
from routes import product, order
from fastapi.responses import HTMLResponse
from database import db

app = FastAPI()

@app.get("/products-view", response_class=HTMLResponse)
def view_products():
    products = list(db.products.find())
    html = "<h2>Product List</h2><ul>"
    for product in products:
        html += f"<li><strong>{product['name']}</strong>: ₹{product['price']}</li>"
    html += "</ul>"
    return html

@app.get("/")
def read_root():
    return {"message": "Welcome to the eCommerce FastAPI backend!"}

app.include_router(product.router)
app.include_router(order.router)
