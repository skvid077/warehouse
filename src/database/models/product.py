from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base, str_50


class Product(Base):
    __tablename__ = 'Product'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str_50] = mapped_column(nullable=False)
    description: Mapped[str_50] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)
