from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str

class Order(BaseModel):
    id: int
    product_name: str
    product_count: int
    is_cancelled: bool = False
    user_id: int
