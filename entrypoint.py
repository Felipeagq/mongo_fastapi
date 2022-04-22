from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_check():
    return "v0.0.0"