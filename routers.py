from fastapi import APIRouter, HTTPException, Path, Query
from models import User, Order
from typing import List
users_router = APIRouter(prefix="/users")
orders_router = APIRouter(prefix="/orders")
users: List[User] = []
orders = {}


@users_router.post("/", response_model=int)
def create_user(user_name:str) -> int:
    user_id = len(users)
    user_sign = User(id=user_id,name=user_name)
    users.append(user_sign)
    return user_id


@users_router.get("/{user_id}", response_model=User)
def get_user(user_id: int = Path(...)) -> User:
    try:
        return users[user_id]
    except HTTPException:
        raise HTTPException(status_code=404, detail="User not found")


@orders_router.post("/", response_model=int)
def create_order(user_id_: int, product_name_: str, product_count_: int) -> int:
    if user_id_ >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    order_id = len(orders)
    order_sign = Order(id=order_id, user_id=user_id_, product_name=product_name_, product_count=product_count_)
    orders[order_id] = order_sign
    return order_id


@orders_router.patch("/{order_id}", response_model=str)
def cancel_order(order_id: int = Path(...)) -> str:
    if order_id not in orders.keys():
        raise HTTPException(status_code=404, detail="Order not found")
    orders[order_id].is_cancelled = True
    return "Cancelled successfully"


@orders_router.delete("/{order_id}", response_model=str)
def delete_order(order_id: int = Path(...)) -> str:
    if order_id not in orders.keys():
        raise HTTPException(status_code=404, detail="Order not found")
    orders.pop(order_id)
    return "Deleted successfully"


@orders_router.get("/{order_id}", response_model=int)
def get_order(order_id: int = Path(...), product_name: str = Query(...), is_cancelled: bool = Query(...)):
    return orders[order_id].product_count

