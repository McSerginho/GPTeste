from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "API funcionando!"}

@app.get("/teste")
async def read_teste():
    return {"message": "Deu certo, ufa kkk"}
