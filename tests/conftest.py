import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from src import app
from src.core.config import config
from src.core.db.session import Base, get_db
from sqlalchemy.orm import Session

from src.shortener.models import ShortUrl
from src.shortener.repositories import ShorterRepo
from src.shortener.services import ShorterService

@pytest.fixture(scope="session")
def db_engine():
    """
    Create engine with db test
    """
    engine = create_engine(config.SQLALCHEMY_DATABASE_URL_TEST, connect_args={
        "check_same_thread": False})

    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def db(db_engine):
    """
    Create connection with db test
    """
    connection = db_engine.connect()

    transaction = connection.begin()
    db = Session(bind=connection)

    yield db

    db.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(db):
    """
    Return an API Client
    """
    app.dependency_overrides = {}
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def repository(db):
    """
    Return an repository
    """
    
    yield ShorterRepo(db)
        
@pytest.fixture(scope="function")
def service(repository):
    """
    Return service
    """

    yield ShorterService(repository)
    
@pytest.fixture
def shorturl(db):
    item = ShortUrl(url="http://www.google.com",shortcode="6VcwJUYK")
    db.add(item)
    db.commit()