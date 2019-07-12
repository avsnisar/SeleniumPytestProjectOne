import pytest
from fixture.Application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled(app):
    app.open_home_page()
    app.session.login("admin", "admin")
    app.session.logout()


if __name__ == "__main__":
    pytest.main()
