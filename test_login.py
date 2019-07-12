import unittest

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

    def tearDown(self):
        self.app.destroy()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
