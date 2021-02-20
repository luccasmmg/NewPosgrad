#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.post_graduations import delete_information, edit_information, get_information, create_scheduled_report
from app.db import models as m

from app.schemas.pg_information_schemas import ScheduledReportCreate, ScheduledReport, ScheduledReportEdit
from app.core.auth import get_current_active_user

scheduled_report_router = s = APIRouter()

@s.post("/defesa", response_model=ScheduledReport, response_model_exclude_none=True)
async def scheduled_report_create(
    request: Request,
    scheduled_report: ScheduledReportCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create new scheduled report
    """
    return create_scheduled_report(db, current_user.owner_id, scheduled_report)

@s.delete("/defesa/{scheduled_report_id}", response_model=ScheduledReport, response_model_exclude_none=True)
async def scheduled_report_delete(
        request: Request,
        scheduled_report_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete scheduled report
    """
    return delete_information(db, get_information(db, scheduled_report_id, m.ScheduledReport).id, m.ScheduledReport)

@s.put("/defesa/{scheduled_report_id}", response_model=ScheduledReport, response_model_exclude_none=True)
async def scheduled_report_edit(
        request: Request,
        scheduled_report_id: int,
        scheduled_report: ScheduledReportEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit scheduled report
    """
    return edit_information(db, get_information(db, scheduled_report_id, m.ScheduledReport).id, scheduled_report, m.ScheduledReport)
