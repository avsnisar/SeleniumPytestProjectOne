from model.film import Film
import pytest


def test_add_movie(app):
    app.movie.create(Film(name="Test", year="1234", description="Goes here"))
    # app.close_alert_and_get_its_text()


if __name__ == "__main__":
    pytest.main()
