from fastapi import APIRouter

from src.database.schemas import Product as Product_pydantic_model

from src.database import Product


router = APIRouter(prefix='/products', tags=['products'])


@router.post('/addition')
async def addition(title: str, description: str, price: float, amount: int) -> str:
    await Product.addition(title=title, description=description, price=price, amount=amount)
    product_id = await Product.current_id()
    return f'Создан продукт под номером {product_id}'


@router.get('/get_all')
async def get_all() -> list[Product_pydantic_model]:
    return await Product.get_all()


@router.get('/get_product/{product_id}')
async def get_order(product_id: int) -> Product_pydantic_model:
    return await Product.get_current(product_id=product_id)


@router.put('/update/{product_id}')
async def update(product_id: int, title: str, description: str, price: float, amount: int) -> str:
    await Product.update(product_id=product_id, title=title, description=description, price=price, amount=amount)
    return 'Данные о продукте обновлены'


@router.delete('/delete/{product_id}')
async def delete(product_id: int) -> str:
    await Product.delete(product_id=product_id)
    return 'Продукт удалён'
