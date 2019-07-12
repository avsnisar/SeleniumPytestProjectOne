from selenium.common.exceptions import UnexpectedAlertPresentException


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "/php4dvd/")

    def login(self, username, password):
        wd = self.app.wd
        try:
            self.open_home_page()
            wd.find_element_by_id("username").clear()
            wd.find_element_by_id("username").send_keys(username)
            wd.find_element_by_name("password").clear()
            wd.find_element_by_name("password").send_keys(password)
            wd.find_element_by_name("submit").click()
        except UnexpectedAlertPresentException as e:
            self.app.wd.close_alert_and_get_its_text()

    def logout(self):
        wd = self.app.wd
        try:
            wd.find_element_by_css_selector("a[href$='?logout']").click()
            alert = self.app.wd.switch_to.alert
            alert.accept()

        except UnexpectedAlertPresentException as e:
            print(e.stacktrace)
