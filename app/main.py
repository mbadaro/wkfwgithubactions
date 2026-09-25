# app/main.py
from fastapi import FastAPI

app = FastAPI(title="Minha API")


@app.get("/")
def raiz():
    return {"mensagem": "Ola, mundo!"}


@app.get("/saude")
def saude():
    return {"status": "ok"}


@app.get("/soma/{a}/{b}")
def soma(a: int, b: int):
    return {"resultado": a + b}
