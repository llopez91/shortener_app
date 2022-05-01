from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.core.db.session import Base, engine
from src.routers import router
from src.core.exceptions.base import CustomException
import src.shortener.models

def init_routers(app: FastAPI):
    """ Load routers """
    app.include_router(router)


def init_listeners(app: FastAPI):
    """ Exceptions Handler """
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )

def init_db():
    """ Init Database and Tables"""
    Base.metadata.create_all(bind=engine)

def create_app():
    app = FastAPI(
        title="Shortener",
        description="Shortener APP",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    init_routers(app)
    init_listeners(app)
    init_db()
    return app


app = create_app()