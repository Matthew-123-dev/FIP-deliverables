from fastapi import FastAPI
from contextlib import asynccontextmanager
from .config import settings
from .routers import students, search, ai
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # place for startup/shutdown hooks
    yield


def create_app() -> FastAPI:
    app = FastAPI(title="Student Records API", version="1.0.0", description="Async Student Records Management API", lifespan=lifespan)

    if settings.APP_ENV == "development":
        app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

    app.include_router(students.router, prefix="/api/v1/students", tags=["students"])
    app.include_router(search.router, prefix="/api/v1/search", tags=["search"])
    app.include_router(ai.router, prefix="/api/v1/students", tags=["ai"])

    @app.get("/health")
    async def health():
        return {"status": "ok", "version": "1.0.0"}

    return app


app = create_app()
