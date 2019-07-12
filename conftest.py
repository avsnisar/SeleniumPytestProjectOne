import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="admin")

    def remove_session():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(remove_session)
    return fixture
