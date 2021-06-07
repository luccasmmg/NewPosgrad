from fastapi import APIRouter, Request, Depends, Response, encoders, Form, File, UploadFile, HTTPException
import typing as t
import boto3
from os.path import splitext

from app.db.session import get_db
from app.db.crud.post_graduations import get_informations, delete_information, edit_information, get_information, create_covenant
from app.db import models as m

from app.schemas.pg_information_schemas import CovenantCreate, Covenant, CovenantEdit
from app.core.auth import get_current_active_user

covenant_router = c = APIRouter()

@c.get("/convenio", response_model=t.List[Covenant], response_model_exclude_none=True)
async def get_covenants(
        response: Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    covenants = get_informations(db, current_user.owner_id, m.Covenant).all()
    response.headers["Content-Range"] = f"0-9/{len(covenants)}"
    return covenants

@c.get("/convenio/{covenant_id}", response_model=Covenant, response_model_exclude_none=True)
async def covenant_details(
        response: Response,
        covenant_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    return get_information(db, covenant_id, m.Covenant)

@c.post("/convenio", response_model=Covenant, response_model_exclude_none=True)
async def covenant_create(
    request: Request,
    db=Depends(get_db),
    name: str = Form(...),
    object: str = Form(...),
    initials: str = Form(...),
    logo_file: UploadFile = File(...),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new covenants
    """
    if not logo_file.filename.endswith(('.jpg', '.jpeg', '.png')):
        raise HTTPException(status_code=422, detail="The logo file has to be in .jpg .jpeg or .png")

    filename_normalized = "".join(x for x in splitext(logo_file.filename)[0] if x.isalnum()) + splitext(logo_file.filename)[1]

    s3_response = boto3.resource('s3').Bucket('juno-minerva').put_object(Key=f'logo_covenants/{filename_normalized}', Body=logo_file.file, ACL='public-read')

    covenant = CovenantCreate(object=object, name=name, initials=initials, logo_file=f'https://juno-minerva.s3-sa-east-1.amazonaws.com/logo_covenants/{filename_normalized}')

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
    return delete_information(db, get_information(db, covenant_id, m.Covenant).id, m.Covenant)

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
    return edit_information(db, get_information(db, covenant_id, m.Covenant).id, covenant, m.Covenant)
