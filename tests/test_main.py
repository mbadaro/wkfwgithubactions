# tests/test_main.py
from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)


def test_raiz():
    resposta = cliente.get("/")
    assert resposta.status_code == 200
    assert resposta.json() == {"mensagem": "Ola, mundo!"}


def test_saude():
    resposta = cliente.get("/saude")
    assert resposta.status_code == 200
    assert resposta.json()["status"] == "ok"


def test_soma():
    resposta = cliente.get("/soma/2/3")
    assert resposta.status_code == 200
    assert resposta.json() == {"resultado": 5}


def test_soma_com_negativos():
    resposta = cliente.get("/soma/-4/1")
    assert resposta.status_code == 200
    assert resposta.json() == {"resultado": -3}


def test_soma_rejeita_nao_inteiro():
    resposta = cliente.get("/soma/2/abc")
    assert resposta.status_code == 422
