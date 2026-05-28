from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import database
from users import entity as users_entity
from users.routes import router as users_router
from restaurants import entity as restaurants_entity
from restaurants.routes import router as restaurants_router
from orders import entity as orders_entity
from orders.routes import router as orders_router
from delivery import entity as delivery_entity
from delivery.routes import router as delivery_router
from payments import entity as payments_entity
from payments.routes import router as payments_router

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent

database.Base.metadata.create_all(bind=database.engine)

app.include_router(users_router)
app.include_router(restaurants_router)
app.include_router(delivery_router)
app.include_router(orders_router)
app.include_router(payments_router)

app.mount("/frontend", StaticFiles(directory=BASE_DIR / "frontend"), name="frontend")


@app.get("/", include_in_schema=False)
def frontend():
    return FileResponse(BASE_DIR / "frontend" / "index.html")
