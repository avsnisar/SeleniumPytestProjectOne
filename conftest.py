import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:

        fixture = Application()
        fixture.session.login(username="admin", password="admin")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def remove_session():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(remove_session)
    return fixture
