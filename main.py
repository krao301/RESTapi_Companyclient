from fastapi import FastAPI
from routes.clientinfo_routes import client_api_router
app = FastAPI()

app.include_router(client_api_router)