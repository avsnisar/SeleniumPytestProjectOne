import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_logout(app):
    app.session.login("admin", "admin")
    app.session.logout()


if __name__ == "__main__":
    pytest.main()
