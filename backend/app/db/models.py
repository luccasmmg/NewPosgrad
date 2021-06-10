import enum

from sqlalchemy import Boolean, Column, Integer, String, Text, ForeignKey, Enum, Date, DateTime, func
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
    impact = relationship("Impact", back_populates="post_graduation_owner")
    researchers = relationship("Researcher", back_populates="post_graduation_owner")
    covenants = relationship("Covenant", back_populates="post_graduation_owner")
    participations = relationship("Participation", back_populates="post_graduation_owner")
    attendance = relationship("Attendance", uselist=False, back_populates="post_graduation_owner")
    official_documents = relationship("OfficialDocument", back_populates="post_graduation_owner")
    news = relationship("News", back_populates="post_graduation_owner")
    events = relationship("Event", back_populates="post_graduation_owner")
    repository_docs = relationship("Repository", back_populates="post_graduation_owner")
    scheduled_reports = relationship("ScheduledReport", back_populates="post_graduation_owner")
    advisors = relationship("StudentAdvisor", back_populates="post_graduation_owner")
    staff = relationship("Staff", back_populates="post_graduation_owner")
    projects = relationship("Project", back_populates="post_graduation_owner")

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

class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    coordinator = Column(Integer, ForeignKey("researcher.id"))
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    email = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    deleted = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="projects")
    coordinator_data = relationship("Researcher", back_populates="projects")

class CourseType(str, enum.Enum):
    masters = 'masters'
    doctorate = 'doctorate'

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    name = Column(String, nullable=False)
    institutional_repository_url = Column(String, nullable=False)
    id_sigaa = Column(Integer, unique=True, nullable=False)
    course_type = Column(Enum(CourseType), nullable=False)
    deleted = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="courses")

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    email = Column(String)
    location = Column(String)
    schedule = Column(String)
    about = Column(String)
    deleted = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="attendance")
    phones = relationship("Phone", back_populates="attendance_owner")

class PhoneType(str, enum.Enum):
    fixed = 'fixed'
    cellphone = 'cellphone'

class Phone(Base):
    __tablename__ = "phone"

    id = Column(Integer, primary_key=True, index=True)
    owner_attendance_id = Column(Integer, ForeignKey("attendance.id"))
    number = Column(Integer, unique=True, nullable=False)
    phone_type = Column(Enum(PhoneType), nullable=False)
    deleted = Column(Boolean, default=False)

    attendance_owner = relationship("Attendance", back_populates="phones")

class Researcher(Base):
    __tablename__ = "researcher"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    name = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    deleted = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="researchers")
    projects = relationship("Project", back_populates="coordinator_data")

class Covenant(Base):
    __tablename__ = "covenant"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    name = Column(String, nullable=False)
    initials = Column(String, nullable=False)
    logo_file = Column(String)
    object = Column(String)
    deleted = Column(Boolean, default=False)
    finished = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="covenants")

class ParternshipCategory(str, enum.Enum):
    cooperation_agreement = 'cooperation_agreement'
    prize = 'prize'
    event = 'event'
    parternship = 'parternship'
    posdoc = 'posdoc'

class Participation(Base):
    __tablename__ = "participation"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    title = Column(String, nullable=False)
    description = Column(String)
    year = Column(Integer)
    international = Column(Boolean)
    location = Column(String, nullable=False)
    category = Column(Enum(ParternshipCategory), nullable=False)
    deleted = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="participations")

class DocumentCategory(str, enum.Enum):
    regiments = 'regiments'
    records = 'records'
    resolutions = 'resolutions'
    plans = 'plans'
    others = 'others'

class OfficialDocument(Base):
    __tablename__ = "official_document"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    title = Column(String, nullable=False)
    file = Column(String, nullable=False)
    cod = Column(String, nullable=False)
    category = Column(Enum(DocumentCategory), nullable=False)
    deleted = Column(Boolean, default=False)
    inserted_on = Column(DateTime(timezone=True), server_default=func.now())

    post_graduation_owner = relationship("PostGraduation", back_populates="official_documents")

class Rank(str, enum.Enum):
    coordinator = 'coordinator'
    vice_coordinator = 'vice_coordinator'
    secretariat = 'secretariat'
    intern = 'intern'

class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    name = Column(String, nullable=False)
    rank = Column(Enum(Rank), nullable=False)
    description = Column(Text)
    photo = Column(String)
    deleted = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="staff")

class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    title = Column(String, nullable=False)
    link = Column(String)
    initial_date = Column(DateTime(timezone=True))
    final_date = Column(DateTime(timezone=True))
    deleted = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="events")

class Repository(Base):
    __tablename__ = "repository"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    title = Column(String)
    link = Column(String)
    year = Column(Integer)
    author = Column(String)
    deleted = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="repository_docs")

class ScheduledReport(Base):
    __tablename__ = "scheduled_report"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    location = Column(String)
    datetime = Column(DateTime(timezone=True))
    deleted = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="scheduled_reports")

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    title = Column(String, nullable=False)
    headline = Column(String)
    body = Column(Text)
    deleted = Column(Boolean, default=False)
    date = Column(Date)

    post_graduation_owner = relationship("PostGraduation", back_populates="news")

class Impact(Base):
    __tablename__ = "impact"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    body = Column(Text)
    deleted = Column(Boolean, default=False)
    inserted_on = Column(DateTime(timezone=True), server_default=func.now())

    post_graduation_owner = relationship("PostGraduation", back_populates="impact")

class StudentAdvisor(Base):
    __tablename__ = "student_advisor"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("post_graduation.id"))
    registration = Column(String, nullable=False)
    advisor_name = Column(String, nullable=False)
    deleted = Column(Boolean, default=False)

    post_graduation_owner = relationship("PostGraduation", back_populates="advisors")
