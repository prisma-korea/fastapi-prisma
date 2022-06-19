from src.apis import apis
from typing import Union
from src.prisma import prisma

from fastapi import FastAPI

app = FastAPI()
# app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(apis, prefix="/apis")


@app.on_event("startup")
async def startup():
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()


@app.get("/")
def read_root():
    return {"version": "1.0.0"}
