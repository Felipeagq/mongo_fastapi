from fastapi import FastAPI
from router import router

app = FastAPI()

@app.get("/")
async def hello_check():
    return "v0.0.0"


app.include_router(router=router)