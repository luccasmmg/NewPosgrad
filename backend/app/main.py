from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
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
from app.api.api_v1.routers.repository import repository_doc_router
from app.api.api_v1.routers.scheduled_report import scheduled_report_router
from app.api.api_v1.routers.student_advisor import student_advisor_router
from app.api.api_v1.routers.staff import staff_router
from app.api.api_v1.routers.project import project_router
from app.api.api_v1.routers.project_member import project_member_router
from app.api.api_v1.routers.impact import impact_router

from app.core import config
from app.db.session import SessionLocal
from app.core.auth import get_current_active_user
from app.core.celery_app import celery_app
from app.core.api_ufrn import get_public_data
from app.core.utils.cache import new_key_builder
from app import tasks

import aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

app = FastAPI(
    title=config.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api"
)

origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response

@app.on_event("startup")
async def startup():
    redis = await aioredis.create_redis_pool("redis://redis", encoding="utf8")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache", key_builder=new_key_builder)

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
app.include_router(repository_doc_router, prefix="/api/v1", tags=["repository_docs"])
app.include_router(scheduled_report_router, prefix="/api/v1", tags=["scheduled reports"])
app.include_router(student_advisor_router, prefix="/api/v1", tags=["student advisor"])
app.include_router(impact_router, prefix="/api/v1", tags=["impact"])
app.include_router(staff_router, prefix="/api/v1", tags=["staff"])
app.include_router(project_router, prefix="/api/v1", tags=["project"])
app.include_router(project_member_router, prefix="/api/v1", tags=["project"])
app.include_router(public_router, prefix="/api/v1/publico", tags=["public"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
