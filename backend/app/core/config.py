import os

PROJECT_NAME = "posgrad"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

API_V1_STR = "/api/v1"

API_URL_ROOT           = 'https://api.info.ufrn.br/'
API_TOKEN_ROOT         = 'https://autenticacao.info.ufrn.br/'
AUTHORIZATION_ENDPOINT = f"{API_URL_ROOT}authz-server/oauth/authorize"
TOKEN_ENDPOINT         = f"{API_TOKEN_ROOT}authz-server/oauth/token"
