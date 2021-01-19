from pydantic import BaseModel, Field
import typing as t

# User schemes

class UserBase(BaseModel):
    email: str
    owner_id: int
    is_active: bool = True
    is_superuser: bool = False
    first_name: str = None
    last_name: str = None

class UserOut(UserBase):
    pass

class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True

class UserEdit(UserBase):
    password: t.Optional[str] = None

    class Config:
        orm_mode = True

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Authentication schemes

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenUFRN(Token):
    expires_in: float

class TokenData(BaseModel):
    email: str = None
    permissions: str = "user"

class SinfoKeys(BaseModel):
   client_id: str = Field(alias='client-id')
   client_secret: str = Field(alias='client-secret')
   x_api_key: str = Field(alias='x-api-key')

class GoogleMapsKeys(BaseModel):
    key: str

# PostGraduation schemes

class PostGraduationBase(BaseModel):
    id_unit: int
    name: str
    initials: str
    sigaa_code: str
    is_signed_in: str = True
    old_url: str = ""
    description_small: str = ""
    description_big: str = ""

class PostGraduationCreate(PostGraduationBase):
    pass

class PostGraduation(PostGraduationBase):
    id: int
    users: t.List[User] = []

    class Config:
        orm_mode = True
