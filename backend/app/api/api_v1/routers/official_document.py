#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders, Form, File, UploadFile, HTTPException
import typing as t
import boto3

from app.db.session import get_db
from app.db.crud.post_graduations import delete_information, edit_information, get_information, create_official_document
from app.db import models as m

from app.schemas.pg_information_schemas import OfficialDocumentCreate, OfficialDocument, OfficialDocumentEdit
from app.core.auth import get_current_active_user

document_router = d = APIRouter()

@d.post("/documento", response_model=OfficialDocument, response_model_exclude_none=True)
async def official_document_create(
    request: Request,
    db=Depends(get_db),
    title: str = Form(...),
    cod: str = Form(...),
    category: str = Form(...),
    file: UploadFile = File(...),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new official documents
    """
    if not file.filename.endswith(('.pdf', '.docx', '.odt')):
        raise HTTPException(status_code=422, detail="The logo file has to be in .pdf .docx or .odt")

    s3_response = boto3.resource('s3').Bucket('juno-minerva').put_object(Key=f'documents/{category}/{file.filename}', Body=file.file, ACL='public-read')

    official_document = OfficialDocumentCreate(title=title,
                                               cod=cod,
                                               category=category,
                                               file=f'https://juno-minerva.s3-sa-east-1.amazonaws.com/documents/{category}/{file.filename}',
                                               )

    return create_official_document(db, current_user.owner_id, official_document)

@d.delete("/documento/{official_document_id}", response_model=OfficialDocument, response_model_exclude_none=True)
async def official_document_delete(
        request: Request,
        official_document_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete Official Document
    """
    return delete_information(db, get_information(db, official_document_id, m.OfficialDocument).id, m.OfficialDocument)

@d.put("/documento/{official_document_id}", response_model=OfficialDocument, response_model_exclude_none=True)
async def official_document_edit(
        request: Request,
        official_document_id: int,
        official_document: OfficialDocumentEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit Official Document
    """
    return edit_information(db, get_information(db, official_document_id, m.OfficialDocument).id, official_document, m.OfficialDocument)
