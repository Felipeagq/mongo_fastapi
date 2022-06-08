from fastapi import FastAPI
import uvicorn
from app.config.settings import settings
from app.routes.router import router as mongo_crud_router


app = FastAPI(
    title="Mongo CRUD",
    version="V0.0.1"
)

@app.get("/")
async def hello_check():
    return "v0.0.0"


app.include_router(
    mongo_crud_router,
    prefix=settings.API_V1_STR,
    tags=["Mongo CRUD Routes"]
)


if __name__ == "__main__":
    uvicorn.run(
        "entrypoint:app",
        host="0.0.0.0",
        port=5000,
        workers=1,
        reload=True,
        log_level="info",
        use_colors=False
    )