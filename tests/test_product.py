from src.database import Product


async def test_addition(title='mazik', description='vkusni mazik', price=10.0, amount=10):
    res_start = await Product.current_id()
    await Product.addition(title=title, description=description, price=price, amount=amount)
    res_finish = await Product.current_id()
    await Product.delete(product_id=res_finish)
    assert res_start != res_finish


async def test_get_all(title='mazik', description='vkusni mazik', price=10.0, amount=10):
    product_ids = list()
    for i in range(5):
        await Product.addition(title=title, description=description, price=price, amount=amount)
        product_ids.append(await Product.current_id())
    res = await Product.get_all()
    for product_id in product_ids:
        await Product.delete(product_id=product_id)
    assert len(res) == 5


async def test_get_order(title='mazik', description='vkusni mazik', price=10.0, amount=10):
    await Product.addition(title=title, description=description, price=price, amount=amount)
    product_id = await Product.current_id()
    res = await Product.get_current(product_id=product_id)
    await Product.delete(product_id=product_id)
    assert res is not None


async def test_update(title='mazik', description='vkusni mazik', price=10.0, amount=10):
    await Product.addition(title=title, description=description, price=price, amount=amount)
    product_id = await Product.current_id()
    res1 = await Product.get_current(product_id=product_id)
    title = 'no mazik'
    description = 'no vkusna'
    price = 1.0
    amount = 1000
    await Product.update(product_id=product_id, title=title, description=description, price=price, amount=amount)
    res2 = await Product.get_current(product_id=product_id)
    await Product.delete(product_id=product_id)
    assert res1 != res2


async def test_delete(title='mazik', description='vkusni mazik', price=10.0, amount=10):
    await Product.addition(title=title, description=description, price=price, amount=amount)
    product_id_start = await Product.current_id()
    await Product.delete(product_id=product_id_start)
    product_id_finish = await Product.current_id()
    assert product_id_start != product_id_finish
