from pydantic import BaseModel

from src.database.schemas.pydantic.product import Product


class OrderItem(BaseModel):
    id: int
    product_id: int | None
    order_id: int | None
    amount: int
    product: 'Product' = None
