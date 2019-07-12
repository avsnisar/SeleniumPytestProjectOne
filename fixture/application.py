from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from movie.movie import MovieHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)
        self.movie = MovieHelper(self)

    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.wd.switch_to.alert
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #     finally:
    #         self.accept_next_alert = True

    def destroy(self):
        wd = self.wd
        wd.quit()
        # self.wd.assertEqual([], self.verificationErrors)
