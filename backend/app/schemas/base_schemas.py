from pydantic import BaseModel, Field, EmailStr, HttpUrl
from app.db.models import CourseType, PhoneType
import typing as t

# User schemes

class UserBase(BaseModel):
    email: EmailStr
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

# Course schemes

class CourseBase(BaseModel):
    owner_id: int
    name: str
    institutional_repository_url: HttpUrl
    id_sigaa: int
    course_type: CourseType

class CourseCreate(CourseBase):
    pass

class CourseEdit(CourseBase):
    pass

class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True

# Phone schemes

class PhoneBase(BaseModel):
    number: int
    phone_type: PhoneType

class PhoneCreate(PhoneBase):
    pass

class PhoneEdit(PhoneBase):
    pass

class Phone(PhoneBase):
    id: int
    owner_attendance_id: int
    deleted: bool

    class Config:
        orm_mode = True

# Attendance schemes

class AttendanceBase(BaseModel):
    email: EmailStr
    location: str
    schedule: str

class AttendanceCreate(AttendanceBase):
    owner_id: int
    pass

class AttendanceEdit(AttendanceBase):
    pass

class Attendance(AttendanceBase):
    owner_id: int
    id: int
    phones: t.List[Phone] = []

    class Config:
        orm_mode = True

# PostGraduation schemes

class PostGraduationBase(BaseModel):
    id_unit: int
    name: str
    initials: str
    sigaa_code: int
    is_signed_in: t.Optional[bool] = True
    old_url: t.Optional[str] = ""
    description_small: t.Optional[str] = ""
    description_big: t.Optional[str] = ""

class PostGraduationCreate(PostGraduationBase):
    pass

class PostGraduationEdit(PostGraduationBase):
    pass

class PostGraduation(PostGraduationBase):
    id: int
    users: t.List[User] = []
    courses: t.List[Course] = []
    attendance: Attendance = None

    class Config:
        orm_mode = True
