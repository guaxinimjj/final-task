from department_app.config import SECRET_KEY


def test_sample():
    assert SECRET_KEY != "123"
