from fastapi import APIRouter

from src.database.schemas import Order as Order_model
from src.database.schemas import StatusOrder

from src.database import Order
from src.database import Product

router = APIRouter(prefix='/orders', tags=['orders'])


@router.post('/create_new')
async def create_new() -> str:
    await Order.addition()
    order_id = await Order.current_id()
    return f'Создан заказ под номером {order_id}'


@router.post('/addition_product')
async def addition(order_id: int, product_id: int, amount: int) -> str:
    amount_in_stock = await Product.get_amount(product_id=product_id)
    if amount > amount_in_stock:
        return 'Недостаточно товаров на складе'
    await Order.addition_product_in_order(product_id=product_id, order_id=order_id, amount=amount)
    await Product.update_amount(product_id=product_id, product_amount=amount_in_stock - amount)
    return f'Товар номер {product_id} добавлен в заказ номер {order_id} в количестве: {amount}'


@router.get('/get_all')
async def get_all() -> list[Order_model]:
    return await Order.get_all()


@router.get('/get_order/{order_id}')
async def get_order(order_id: int) -> Order_model:
    return await Order.get_current(order_id=order_id)


@router.patch('/update_status/{order_id}/status')
async def update_status(order_id: int, new_status: StatusOrder) -> str:
    await Order.update(order_id=order_id, status=new_status)
    return f'Статус у заказа {order_id} обновлен'
