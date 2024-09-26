from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class OrderItem(Base):
    __tablename__ = 'OrderItem'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey(column='Product.id', ondelete='SET NULL'), nullable=True)
    order_id: Mapped[int] = mapped_column(ForeignKey(column='Order.id', ondelete='SET NULL'), nullable=True)
    amount: Mapped[int] = mapped_column(nullable=False)
    order: Mapped['Order'] = relationship(
        back_populates='products'
    )
