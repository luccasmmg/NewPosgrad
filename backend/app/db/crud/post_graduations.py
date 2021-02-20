#!/usr/bin/env python3

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t
import enum

from .. import models
from app.schemas import base_schemas
from app.schemas import pg_information_schemas

def get_post_graduation(db: Session, post_graduation_id: int) -> base_schemas.PostGraduation:
    post_graduation = db.query(models.PostGraduation).filter(models.PostGraduation.id == post_graduation_id).first()
    if not post_graduation:
        raise HTTPException(status_code=404, detail="Post Graduation not found")
    return post_graduation

def get_post_graduation_by_initials(db: Session, initials: str) -> base_schemas.PostGraduation:
    post_graduation = db.query(models.PostGraduation).filter(models.PostGraduation.initials == initials).first()
    if not post_graduation:
        raise HTTPException(status_code=404, detail="Post Graduation not found")
    return post_graduation

def create_post_graduation(db: Session, post_graduation: base_schemas.PostGraduationCreate):
    db_post_graduation = models.PostGraduation(
        id_unit=post_graduation.id_unit,
        name=post_graduation.name,
        initials=post_graduation.initials,
        sigaa_code=post_graduation.sigaa_code,
        is_signed_in=post_graduation.is_signed_in,
        old_url=post_graduation.old_url,
        description_small=post_graduation.description_small,
        description_big=post_graduation.description_big,
    )
    db.add(db_post_graduation)
    db.commit()
    db.refresh(db_post_graduation)
    return db_post_graduation

def edit_post_graduation(
        db: Session, post_graduation_id: int, post_graduation: base_schemas.PostGraduationEdit
) -> base_schemas.PostGraduation:
    db_post_graduation = get_post_graduation(db, post_graduation_id)
    update_data = post_graduation.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_post_graduation, key, value)

    db.add(db_post_graduation)
    db.commit()
    db.refresh(db_post_graduation)
    return db_post_graduation

def get_informations(db: Session, pg_id: int, model):
    informations = db.query(model).filter(
        model.owner_id == pg_id).filter(model.deleted == False)
    return informations

def get_information(db: Session, information_id: int, model):
    information = db.query(model).filter(
        model.id == information_id).filter(model.deleted == False).first()
    return information

def delete_information(db: Session, information_id: int, model):
    information = get_information(db, information_id, model)
    if not information:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="information not found")
    setattr(information, "deleted", True)
    db.add(information)
    db.commit()
    db.refresh(information)
    return information

def edit_information(db: Session, information_id: int, information, model):
    db_information = get_information(db, information_id, model)
    update_data = information.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_information, key, value)

    db.add(db_information)
    db.commit()
    db.refresh(db_information)
    return db_information

def add_information(db: Session, model):
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

def create_researcher(db: Session, pg_id: int, researcher: pg_information_schemas.ResearcherCreate):
    db_researcher = models.Researcher(
        owner_id=pg_id,
        cpf=researcher.cpf,
        name=researcher.name,
    )
    return add_information(db, db_researcher)

def create_covenant(db: Session, pg_id: int, covenant: pg_information_schemas.CovenantCreate):
    db_covenant = models.Covenant(
        owner_id=pg_id,
        initials=covenant.initials,
        logo_file=covenant.logo_file,
        name=covenant.name,
    )
    return add_information(db, db_covenant)

def create_participation(db: Session, pg_id: int, participation: pg_information_schemas.ParticipationCreate):
    db_participation = models.Participation(
        owner_id=pg_id,
        title=participation.title,
        description=participation.description,
        year=participation.year,
        international=participation.international,
    )
    return add_information(db, db_participation)

def create_course(db: Session, course: base_schemas.CourseCreate):
    db_course = models.Course(
        name=course.name,
        owner_id=course.owner_id,
        id_sigaa=course.id_sigaa,
        course_type=course.course_type
    )
    return add_information(db, db_course)

def create_attendance(db: Session, attendance: base_schemas.AttendanceCreate):
    db_attendance = models.Attendance(
        owner_id=attendance.owner_id,
        email=attendance.email,
        location=attendance.location,
        schedule=attendance.schedule,
    )
    return add_information(db, db_attendance)

def create_phone(db: Session, attendance_id: int, phone: base_schemas.PhoneCreate):
    db_phone = models.Phone(
        owner_attendance_id=attendance_id,
        number=phone.number,
        phone_type=phone.phone_type,
    )
    return add_information(db, db_phone)

def create_official_document(db: Session, pg_id: int, official_document: pg_information_schemas.OfficialDocumentCreate):
    db_official_document = models.OfficialDocument(
        owner_id=pg_id,
        title=official_document.title,
        category=official_document.category,
        file=official_document.file,
        cod=official_document.cod
    )
    return add_information(db, db_official_document)

def create_news(db: Session, pg_id: int, news: pg_information_schemas.NewsCreate):
    db_news = models.News(
        owner_id=pg_id,
        title=news.title,
        date=news.date,
        headline=news.headline,
        body=news.body
    )
    return add_information(db, db_news)

def create_event(db: Session, pg_id: int, event: pg_information_schemas.EventCreate):
    db_event = models.Event(
        owner_id=pg_id,
        title=event.title,
        link=event.link,
        initial_date=event.initial_date,
        final_date=event.final_date,
    )
    return add_information(db, db_event)

def create_scheduled_report(db: Session, pg_id: int, scheduled_report: pg_information_schemas.ScheduledReportCreate):
    db_scheduled_report = models.ScheduledReport(
        owner_id=pg_id,
        title=scheduled_report.title,
        author=scheduled_report.author,
        location=scheduled_report.location,
        datetime=scheduled_report.datetime,
    )
    return add_information(db, db_scheduled_report)
