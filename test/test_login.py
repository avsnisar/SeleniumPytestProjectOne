import pytest
from fixture.application import Application
from model.film import Film


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_logout(app):
    app.session.login("admin", "admin")
    app.session.logout()


def test_add_movie(app):
    app.session.login("admin", "admin")
    app.movie.create(Film(name="Test", year="1234", description="Goes here"))
    app.session.logout()


if __name__ == "__main__":
    pytest.main()
