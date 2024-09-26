from datetime import datetime

from pydantic import BaseModel

from src.database.schemas.pydantic.orderitem import OrderItem

from src.database.schemas import StatusOrder as StatusOrder_enum


class Order(BaseModel):
    id: int
    of_creation: datetime
    status: StatusOrder_enum
    products: list['OrderItem']
