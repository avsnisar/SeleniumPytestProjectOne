import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver


class Untitled(unittest.TestCase):
    wd: WebDriver

    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(10)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)

    def login(self, wd):
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("admin")
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("admin")
        wd.find_element_by_name("submit").click()

    def open_home_page(self, wd):
        wd.get(url="http://localhost/php4dvd/")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        wd = self.wd
        wd.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
