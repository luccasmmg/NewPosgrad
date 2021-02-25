#!/usr/bin/env python3
from pydantic import BaseModel

class Professor(BaseModel):
    name: str
    rank: str
    level: str
    phone: str
    lattes: str
    email: str
