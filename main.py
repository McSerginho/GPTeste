from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def read_test():
    return {"message": "Deu certo, ufa kkk"}

# Para executar o servidor
# No terminal, use o seguinte comando:
# uvicorn main:app --reload
