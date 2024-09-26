from sqlalchemy import select, insert, delete, update

from src.database.models.product import Product as Product_model

from src.database.schemas import Product as Product_pydantic_model

from src.database.models import async_session_factory


class Product:

    @staticmethod
    async def addition(title: str, description: str, price: float, amount: int):
        async with async_session_factory() as session:
            query = insert(Product_model).values({
                'title': title,
                'description': description,
                'price': price,
                'amount': amount
            })
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def get_current(product_id: int) -> Product_pydantic_model:
        async with async_session_factory() as session:
            query = select(Product_model).filter_by(id=product_id)
            result = await session.execute(query)
            result = result.scalars().one()
            result = Product_pydantic_model.model_validate(result, from_attributes=True)
        return result

    @staticmethod
    async def get_all() -> list[Product_pydantic_model]:
        async with async_session_factory() as session:
            query = select(Product_model)
            results = await session.execute(query)
            results = results.scalars().all()
            results = [Product_pydantic_model.model_validate(result, from_attributes=True) for result in results]
        return results

    @staticmethod
    async def delete(product_id: int):
        async with async_session_factory() as session:
            query = delete(Product_model).filter_by(id=product_id)
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def update(product_id: int, title: str, description: str, price: float, amount: int):
        async with async_session_factory() as session:
            query = update(Product_model).filter_by(id=product_id).values({
                'title': title,
                'description': description,
                'price': price,
                'amount': amount
            })
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def get_amount(product_id: int):
        async with async_session_factory() as session:
            query = select(Product_model.amount).filter_by(id=product_id)
            result = await session.execute(query)
            result = result.scalars().one()
        return result

    @staticmethod
    async def update_amount(product_id: int, product_amount: int):
        async with async_session_factory() as session:
            query = update(Product_model).filter_by(id=product_id).values({
                'amount': product_amount
            })
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def current_id() -> int:
        async with async_session_factory() as session:
            query = select(Product_model.id)
            result = await session.execute(query)
            result = result.scalars().all()
            result.append(0)
        return max(result)
