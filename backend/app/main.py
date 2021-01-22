from fastapi import FastAPI, Depends
from starlette.requests import Request
import uvicorn

from app.api.api_v1.routers.users import users_router
from app.api.api_v1.routers.auth import auth_router
from app.api.api_v1.routers.post_graduation import post_graduation_router
from app.api.api_v1.routers.api_sistemas import api_sistemas_router
from app.api.api_v1.routers.course import course_router
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


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/task")
async def example_task():
    celery_app.send_task("app.tasks.example_task", args=["Hello World"])

    return {"message": "success"}

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
app.include_router(api_sistemas_router, prefix="/api/v1", tags=["api_sistemas"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
