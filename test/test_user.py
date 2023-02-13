from flask import User
from models import db
import pytest

@pytest.mark.fixture
def app_ctx(app):
    with app.app_context():
        yield


@pytest.mark.usefixtures('app_ctx')
def test_user_model(app):
    user = User()
    db.session.add(user)
    db.session.commit()