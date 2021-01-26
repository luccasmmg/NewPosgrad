import os

PROJECT_NAME = "posgrad"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

S3_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY")
S3_SECRET_ACCESS_KEY= os.getenv("AWS_SECRET_ACCESS_KEY")

API_V1_STR = "/api/v1"

API_URL_ROOT           = 'https://api.ufrn.br/'
API_TOKEN_ROOT         = 'https://autenticacao.ufrn.br/'
AUTHORIZATION_ENDPOINT = f"{API_URL_ROOT}authz-server/oauth/authorize"
TOKEN_ENDPOINT         = f"{API_TOKEN_ROOT}authz-server/oauth/token"
