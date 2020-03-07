import os
import pytest
from app import create_test_app, db
from app.user.routes import user_router


@pytest.fixture(scope='module')
def test_app():
    app = create_test_app()
    app.include_router(user_router())
    yield app  # testing happens here


@pytest.fixture(scope='module')
def test_db():
    db.init_db(os.environ.get('DATABASE_URL_TEST'))
    db.create_all()
    session = db.Session()
    yield session
    session.close()
    db.drop_all()
