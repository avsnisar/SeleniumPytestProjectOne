import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver

from Application import Application


class Untitled(unittest.TestCase):
    wd: WebDriver

    def setUp(self):
        self.app = Application()
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled(self):
        self.app.open_home_page()
        self.app.login("admin", "admin")

    def is_element_present(self, how, what):
        try:
            self.app.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.app.wd.switch_to.alert
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.app.destroy()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
