from fastapi import APIRouter, Request, HTTPException
from bson import ObjectId
from database import db

router = APIRouter()

#  Create Order
@router.post("/orders", status_code=201)
async def create_order(request: Request):
    order_data = await request.json()
    result = db.orders.insert_one(order_data)
    return {"message": "Order created", "id": str(result.inserted_id)}

# List All Orders
@router.get("/orders", status_code=200)
def list_orders(limit: int = 10, offset: int = 0):
    orders = db.orders.find().skip(offset).limit(limit)
    return [{"id": str(o["_id"]), **{k: v for k, v in o.items() if k != "_id"}} for o in orders]

#  Get Order by ID
@router.get("/orders/{order_id}")
def get_order_by_id(order_id: str):
    order = db.orders.find_one({"_id": ObjectId(order_id)})
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order["id"] = str(order["_id"])
    del order["_id"]
    return order

#  Get Orders by user_id
@router.get("/orders/user/{user_id}")
def get_orders_by_user_id(user_id: str):
    orders = db.orders.find({"user_id": user_id})
    result = []
    for order in orders:
        order["id"] = str(order["_id"])
        del order["_id"]
        result.append(order)
    return result

#  Delete Order by ID
@router.delete("/orders/{order_id}", status_code=200)
def delete_order_by_id(order_id: str):
    result = db.orders.delete_one({"_id": ObjectId(order_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully"}

#  Delete All Orders by User ID
@router.delete("/orders/user/{user_id}", status_code=200)
def delete_orders_by_user_id(user_id: str):
    result = db.orders.delete_many({"user_id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="No orders found for this user")
    return {"message": f"Deleted {result.deleted_count} orders for user '{user_id}'"}
