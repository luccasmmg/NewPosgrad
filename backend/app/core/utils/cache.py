from typing import Optional

from starlette.requests import Request
from starlette.responses import Response

def new_key_builder(
    func,
    namespace: Optional[str] = "",
    request: Optional[Request] = None,
    response: Optional[Response] = None,
    args: Optional[tuple] = None,
    kwargs: Optional[dict] = None,
):
    from fastapi_cache import FastAPICache
    new_kwargs = {key:val for key, val in kwargs.items() if key != 'db'}
    prefix = FastAPICache.get_prefix()
    cache_key = f"{prefix}:{namespace}:{func.__module__}:{func.__name__}:{args}:{new_kwargs}"
    return cache_key
