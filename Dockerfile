# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Nao gerar .pyc e nao bufferizar a saida (logs aparecem na hora)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instalar dependencias primeiro (aproveita cache de camadas Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o codigo da aplicacao
COPY app/ ./app/

# Expor a porta e rodar.
# Cada flag e um item da lista, sem espacos dentro da string.
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
