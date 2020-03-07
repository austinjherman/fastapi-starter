from app.user.model import User
from app.user.crud import create


def test_user(test_app, test_db):
    user = User(
        email="test@test.com", password="test", name="test"
    )
    expected = {
        "name": "Test",
        "email": "test@test.com"
    }
    response = create(test_db, user)
    assert response == expected
