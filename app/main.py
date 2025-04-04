from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1.routes import router as api_router

app = FastAPI(title="CVExplore")

app.mount("/", StaticFiles(directory="app/frontend", html=True), name="static")

app.include_router(api_router, prefix="/api/v1")
