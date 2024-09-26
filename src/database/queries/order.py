from datetime import datetime

from sqlalchemy import select, insert, update
from sqlalchemy.orm import selectinload

from src.database.models.order import Order as Order_model
from src.database.models.orderitem import OrderItem as OrderItem_model
from src.database.schemas import StatusOrder as StatusOrder_enumeration

from src.database.schemas import Order as Order_pydantic_model

from src.database.models import async_session_factory

from src.database.queries.product import Product


class Order:

    @staticmethod
    async def addition():
        async with async_session_factory() as session:
            query = insert(Order_model).values({
                'of_creation': datetime.now(),
                'status': StatusOrder_enumeration.processed
            })
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def addition_product_in_order(product_id: int, order_id: int, amount: int):
        async with async_session_factory() as session:
            query = insert(OrderItem_model).values({
                'order_id': order_id,
                'product_id': product_id,
                'amount': amount
            })
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def get_current(order_id: int) -> Order_pydantic_model:
        async with async_session_factory() as session:
            query = select(Order_model).filter_by(id=order_id).options(selectinload(Order_model.products))
            result = await session.execute(query)
            result = result.scalars().one()
            result = Order_pydantic_model.model_validate(result, from_attributes=True)
        for product_i in range(len(result.products)):
            if result.products[product_i].product_id is None:
                continue
            product = await Product.get_current(result.products[product_i].product_id)
            result.products[product_i].product = product
        return result

    @staticmethod
    async def get_all() -> list[Order_pydantic_model]:
        async with async_session_factory() as session:
            query = select(Order_model).options(selectinload(Order_model.products))
            results = await session.execute(query)
            results = results.scalars().all()
            results = [Order_pydantic_model.model_validate(result, from_attributes=True) for result in results]
        for result_i in range(len(results)):
            for product_i in range(len(results[result_i].products)):
                if results[result_i].products[product_i].product_id is None:
                    continue
                product = await Product.get_current(results[result_i].products[product_i].product_id)
                results[result_i].products[product_i].product = product
        return results

    @staticmethod
    async def update(order_id: int, status: StatusOrder_enumeration):
        async with async_session_factory() as session:
            query = update(Order_model).filter_by(id=order_id).values({
                'status': status
            })
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def current_id() -> int:
        async with async_session_factory() as session:
            query = select(Order_model.id)
            result = await session.execute(query)
            result = result.scalars().all()
            result.append(0)
        return max(result)
