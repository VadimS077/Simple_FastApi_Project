import uvicorn
from fastapi import FastAPI
from models import User, Order
from routers import users_router, orders_router
from config import config

app = FastAPI()
app.include_router(users_router)
app.include_router(orders_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=config.server_host, port=config.server_port, reload=True)