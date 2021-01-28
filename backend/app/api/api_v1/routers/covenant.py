from fastapi import APIRouter, Request, Depends, Response, encoders, Form, File, UploadFile, HTTPException
import typing as t
import boto3

from app.db.session import get_db
from app.db.crud.covenants import (
    create_covenant,
    get_covenant,
    delete_covenant,
    edit_covenant
)
from app.schemas.pg_information_schemas import CovenantCreate, Covenant, CovenantEdit
from app.core.auth import get_current_active_user

covenant_router = c = APIRouter()

@c.post("/convenio", response_model=Covenant, response_model_exclude_none=True)
async def covenant_create(
    request: Request,
    db=Depends(get_db),
    name: str = Form(...),
    initials: str = Form(...),
    logo_file: UploadFile = File(...),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new covenants
    """
    if not logo_file.filename.endswith(('.jpg', '.jpeg', '.png')):
        raise HTTPException(status_code=422, detail="The logo file has to be in .jpg .jpeg or .png")

    s3_response = boto3.resource('s3').Bucket('juno-minerva').put_object(Key=f'logo_covenants/{logo_file.filename}', Body=logo_file.file, ACL='public-read')

    covenant = CovenantCreate(name=name, initials=initials, logo_file=f'https://juno-minerva.s3-sa-east-1.amazonaws.com/logo_covenants/{logo_file.filename}')

    return create_covenant(db, current_user.owner_id, covenant)

@c.delete("/convenio/{covenant_id}", response_model=Covenant, response_model_exclude_none=True)
async def covenant_delete(
        request: Request,
        covenant_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete covenant
    """
    return delete_covenant(db, get_covenant(db, covenant_id).id)

@c.put("/convenio/{covenant_id}", response_model=Covenant, response_model_exclude_none=True)
async def covenant_edit(
        request: Request,
        covenant_id: int,
        covenant: CovenantEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit covenant
    """
    return edit_covenant(db, get_covenant(db, covenant_id).id, covenant)
