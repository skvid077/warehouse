import asyncio

from src.database.models.order import Order
from src.database.models.product import Product
from src.database.models.orderitem import OrderItem

from src.database.models.base import async_engine, async_session_factory, Base


async def reload_db():
    async with async_engine.connect() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()


if __name__ == '__main__':
    asyncio.run(reload_db())
