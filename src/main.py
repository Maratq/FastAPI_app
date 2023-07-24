import uvicorn
from fastapi import FastAPI, APIRouter

from src import settings
from src.operations.router import user_router

app = FastAPI(
    title="Social networking app"
)


@app.get('/')
def hello():
    return 'hello'


main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(user_router)
app.include_router(main_api_router)

