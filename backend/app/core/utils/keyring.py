#!/usr/bin/env python3

# A simple 'key ring' script. Read data from json files and return a pydantic model with the api credentials

import json, os
from fastapi import HTTPException
from app.schemas.base_schemas import SinfoKeys, GoogleMapsKeys

ENV_FILE_PATH = f"{os.path.dirname(__file__)}/api_keys.json"

GOOGLE_MAPS = 'google_maps_js_api'
SINFO_API = 'sinfo_api_sistemas'

def decode():
    # reading data from file
    try:
        with open(ENV_FILE_PATH, 'r') as keys_file:
            keys_file_content = keys_file.read()
    except FileNotFoundError:
        raise HTTPException(
            status_code=500,
            detail="There was a problem in trying to access the api keys to perform this operation(File not found)"
        )
    except IOError:
        raise HTTPException(
            status_code=500,
            detail="There was a problem in trying to access the api keys to perform this operation(IO Problem)"
        )

    # decoding full content into a py dict
    try:
        return json.loads(keys_file_content)
    except json.decoder.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="There was a problem in trying to access the api keys to perform this operation(The JSON could not be decoded)"
        )

def get_model(id_key: str):
    try:
        if id_key == SINFO_API:
            return SinfoKeys(**decode()[SINFO_API])
        elif id_key == GOOGLE_MAPS:
            return GoogleMapsKeys(**decode()[GOOGLE_MAPS])
    except KeyError:
        raise HTTPException(
            status_code=500,
            detail="There was a problem in trying to access the api keys to perform this operation(The id key could not be found)"
        )
