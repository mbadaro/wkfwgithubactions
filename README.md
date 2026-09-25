# Minha API

API inicial em FastAPI, usada para demonstrar um pipeline de CI/CD com GitHub Actions.

## Como executar

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Endpoints: `GET /`, `GET /saude`, `GET /soma/{a}/{b}`.

## Desenvolvimento

```bash
pip install -r requirements-dev.txt
```

Os mesmos comandos que o CI executa:

```bash
ruff check .
ruff format --check .
pytest --cov=app --cov-report=term-missing
```

Para corrigir a formatacao automaticamente: `ruff format .`

## Docker

```bash
docker build -t minha-api .
docker run -p 8000:8000 minha-api
```

## O pipeline

`.github/workflows/ci-cd.yml` dispara em push para `main`/`develop` e
em pull request para `main`. Sao quatro estagios encadeados por `needs:`:

1. **test** - matriz Python 3.11 e 3.12, lint/formatacao com ruff e
   testes com cobertura.
2. **build** - constroi a imagem e publica em `ghcr.io`. So roda em
   push, nao em pull request. Usa o `GITHUB_TOKEN` automatico, sem
   precisar de nenhum secret.
3. **deploy-staging** - deploy simulado (`echo`), automatico.
4. **deploy-producao** - deploy simulado, somente na branch `main`.

### Configuracao opcional no GitHub

- **Aprovacao manual em producao**: em *Settings -> Environments*,
  abra o environment `producao` e adicione *Required reviewers*. A
  partir dai o estagio 4 fica pausado esperando aprovacao. Se os
  environments `staging` e `producao` ainda nao existirem, crie-os
  nessa mesma tela.
- **Deploy real na AWS**: os estagios 3 e 4 tem o bloco de
  autenticacao via OIDC comentado. Para ativar, crie um IAM Role com
  trust no OIDC do GitHub, defina as variaveis `AWS_ROLE_STAGING` e
  `AWS_ROLE_PRODUCAO`, e adicione `id-token: write` em `permissions`
  do job.
