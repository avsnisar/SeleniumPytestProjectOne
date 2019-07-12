import pytest


def test_login_logout(app):
    app.session.login("admin", "admin")
    app.session.logout()
    # app.close_alert_and_get_its_text()


if __name__ == "__main__":
    pytest.main()
