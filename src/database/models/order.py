from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base

from src.database.schemas import StatusOrder as StatusOrder_enum


class Order(Base):
    __tablename__ = 'Order'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    of_creation: Mapped[datetime] = mapped_column(nullable=False)
    status: Mapped[StatusOrder_enum] = mapped_column(nullable=False)
    products: Mapped[list['OrderItem']] = relationship(
        back_populates='order'
    )
