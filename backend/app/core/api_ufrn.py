import json, time, os, requests

from fastapi import Depends, HTTPException, status
from app.schemas.base_schemas import TokenUFRN, SinfoKeys
from app.core.config import API_URL_ROOT, API_TOKEN_ROOT, AUTHORIZATION_ENDPOINT, TOKEN_ENDPOINT

from aiohttp import ClientSession

def get_public_data(resource_url: str):
    print(resource_url, flush=True)
    try:
        data = requests.get(resource_url, headers=create_headers()).json()
        return data
    except:
        raise HTTPException(
            status_code=503,
            detail=f"Couldn't access the API Sistemas({resource_url}), that probably means that the error is on SINFO servers"
        )

def create_headers():
    return {
        'Authorization' : 'Bearer ' + retrieve_token().access_token,
        'x-api-key': os.getenv('SINFO_X_API_KEY')
    }

async def get_json(client: ClientSession, url: str, headers: dict) -> bytes:
    async with client.get(url, headers=headers) as response:
        if response.status != 200:
            raise HTTPException(
                status_code=response.status,
                detail=f"Couldn't access the API Sistemas({url}), that probably means that the error is on SINFO servers"
            )
        return await response.read()

async def get_public_data_async(url: str, client: ClientSession, headers: dict):
    response = await get_json(client, url, headers)
    return json.loads(response.decode('utf-8'))

def retrieve_token():
    if get_token_from_os() is not None:
        return get_token_from_os()
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
    client_id = os.getenv('SINFO_CLIENT_ID')
    client_secret = os.getenv('SINFO_CLIENT_SECRET')
    url: str = f"{TOKEN_ENDPOINT}?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials"
    print(url, flush=True)
    return url

def get_token_from_os():
    access_token = os.getenv('BEARER_TOKEN')
    expires_in = os.getenv('EXPIRES_IN')
    if access_token is not None and expires_in is not None:
        if float(expires_in) < time.time():
            return TokenUFRN(access_token=access_token, expires_in=float(expires_in), token_type='Bearer')
    return None
