import json, time, os, requests

from fastapi import Depends, HTTPException, status
from app.schemas.base_schemas import TokenUFRN, SinfoKeys
from app.core.config import API_URL_ROOT, API_TOKEN_ROOT, AUTHORIZATION_ENDPOINT, TOKEN_ENDPOINT
from .utils.keyring import get_model, SINFO_API

def get_public_data(resource_url: str):
    if get_token_from_os() is not None:
        token = get_token_from_os()
    else:
        token = retrieve_token().access_token
    headers = {
        'Authorization' : 'Bearer ' + token,
        'x-api-key': get_model(SINFO_API).x_api_key
    }

    try:
        data = requests.get(resource_url, headers=headers).json()
        return data
    except:
        raise HTTPException(
            status_code=503,
            detail=f"Couldn't access the API Sistemas({resource_url}), that probably means that the error is on SINFO servers"
        )

def retrieve_token():
    try:
        token = TokenUFRN(**requests.post(user_authorization_url()).json())

        os.environ['BEARER_TOKEN'] = token.access_token
        os.environ['EXPIRES_IN'] = str(token.expires_in + time.time())

        return token
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail="Token could't be retrieved, the credentials are probably wrong"
        )
    except:
        raise HTTPException(
            status_code=503,
            detail=f"Couldn't access the API Sistemas({user_authorization_url()}), that probably means that the error is on SINFO servers"
        )

def user_authorization_url():
    keys = get_model(SINFO_API)
    url: str = f"{TOKEN_ENDPOINT}?client_id={keys.client_id}&client_secret={keys.client_secret}&grant_type=client_credentials"
    return url

def get_token_from_os():
    access_token = os.getenv('BEARER_TOKEN')
    expires_in = os.getenv('EXPIRES_IN')
    if access_token is not None and expires_in is not None:
        if float(expires_in) < time.time():
            return TokenUFRN(access_token=access_token, expires_in=float(expires_in), token_type='Bearer')
    return None
