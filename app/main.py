from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth, products, orders

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fidget Toys 3D Store API",
    description="API para e-commerce de fidget toys impressos em 3D",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(orders.router)


@app.get("/")
def root():
    return {"message": "API Fidget Toys 3D está rodando com sucesso!"}
