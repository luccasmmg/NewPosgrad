import enum

from sqlalchemy import Boolean, Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship

from .session import Base

class PostGraduation(Base):
    __tablename__ = "post_graduation"

    id = Column(Integer, primary_key=True, index=True)
    id_unit = Column(Integer, unique=True, index=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    initials = Column(String, unique=True, nullable=False)
    sigaa_code = Column(Integer, unique=True, nullable=False)
    is_signed_in = Column(Boolean, default=True)
    old_url = Column(String, default="")
    description_small = Column(Text, default="")
    description_big = Column(Text, default="")

    users = relationship("User", back_populates="post_graduation_owner")
    courses = relationship("Course", back_populates="post_graduation_owner")
    researchers = relationship("Researcher", back_populates="post_graduation_owner")
    covenants = relationship("Covenant", back_populates="post_graduation_owner")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))

    post_graduation_owner = relationship("PostGraduation", back_populates="users")

class CourseType(str, enum.Enum):
    masters = 'masters'
    doctorate = 'masters'

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    name = Column(String, nullable=False)
    id_sigaa = Column(Integer, unique=True, nullable=False)
    course_type = Column(Enum(CourseType), nullable=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="courses")

class Researcher(Base):
    __tablename__ = "researcher"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    name = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    deleted = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="researchers")

class Covenant(Base):
    __tablename__ = "covenant"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    name = Column(String, nullable=False)
    initials = Column(String, nullable=False)
    logo_file = Column(String)
    deleted = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="covenants")
