from fastapi import FastAPI
from src.app import router_order
from src.app import router_product

app = FastAPI(title='warehouse')

app.include_router(router_order)
app.include_router(router_product)
