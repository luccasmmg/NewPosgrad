from fastapi import FastAPI, Depends
from starlette.requests import Request
import uvicorn

from app.api.api_v1.routers.users import users_router
from app.api.api_v1.routers.auth import auth_router
from app.api.api_v1.routers.post_graduation import post_graduation_router
from app.api.api_v1.routers.public import public_router
from app.api.api_v1.routers.course import course_router
from app.api.api_v1.routers.attendance import attendance_router
from app.api.api_v1.routers.researcher import researcher_router
from app.api.api_v1.routers.covenant import covenant_router
from app.api.api_v1.routers.official_document import document_router
from app.api.api_v1.routers.participation import participation_router
from app.api.api_v1.routers.news import news_router
from app.api.api_v1.routers.event import event_router
from app.api.api_v1.routers.scheduled_report import scheduled_report_router
from app.api.api_v1.routers.student_advisor import student_advisor_router

from app.core import config
from app.db.session import SessionLocal
from app.core.auth import get_current_active_user
from app.core.celery_app import celery_app
from app.core.api_ufrn import get_public_data
from app import tasks

app = FastAPI(
    title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api"
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response

# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(post_graduation_router, prefix="/api/v1", tags=["postgraduation"])
app.include_router(course_router, prefix="/api/v1", tags=["courses"])
app.include_router(attendance_router, prefix="/api/v1", tags=["attendances"])
app.include_router(researcher_router, prefix="/api/v1", tags=["researchers"])
app.include_router(covenant_router, prefix="/api/v1", tags=["covenants"])
app.include_router(participation_router, prefix="/api/v1", tags=["participations"])
app.include_router(document_router, prefix="/api/v1", tags=["documents"])
app.include_router(news_router, prefix="/api/v1", tags=["news"])
app.include_router(event_router, prefix="/api/v1", tags=["events"])
app.include_router(scheduled_report_router, prefix="/api/v1", tags=["scheduled reports"])
app.include_router(student_advisor_router, prefix="/api/v1", tags=["student advisor"])
app.include_router(public_router, prefix="/api/v1/publico", tags=["public"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
