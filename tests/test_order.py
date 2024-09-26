from src.database.schemas import StatusOrder
from src.database import Order
from src.database import Product


async def test_create_new():
    res_start = await Order.current_id()
    await Order.addition()
    res_finish = await Order.current_id()
    assert res_start != res_finish


async def test_addition(title='keptchuk', description='ochen vkusna', price=10.1, amount=11):
    await Order.addition()
    order_id = await Order.current_id()
    product_ids = list()
    for i in range(5):
        await Product.addition(title=title, description=description, price=price, amount=amount)
        product_ids.append(await Product.current_id())
    for product_id in product_ids:
        await Order.addition_product_in_order(order_id=order_id, product_id=product_id, amount=10)
    res = await Order.get_current(order_id=order_id)
    for product_id in product_ids:
        await Product.delete(product_id=product_id)
    assert len(res.products) == 5


async def test_get_all():
    res_start = await Order.current_id()
    for i in range(5):
        await Order.addition()
    res_finish = await Order.current_id()
    assert res_finish - res_start == 5


async def test_get_order(title='keptchuk', description='ochen vkusna', price=10.1, amount=11):
    await Order.addition()
    order_id = await Order.current_id()
    product_ids = list()
    for i in range(5):
        await Product.addition(title=title, description=description, price=price, amount=amount)
        product_ids.append(await Product.current_id())
    for product_id in product_ids:
        await Order.addition_product_in_order(order_id=order_id, product_id=product_id, amount=10)
    res = await Order.get_current(order_id=order_id)
    for product_id in product_ids:
        await Product.delete(product_id=product_id)
    assert len(res.products) == 5


async def test_update_status():
    await Order.addition()
    order_id = await Order.current_id()
    await Order.update(order_id=order_id, status=StatusOrder.accept)
    res = await Order.get_current(order_id=order_id)
    assert res.status == StatusOrder.accept
