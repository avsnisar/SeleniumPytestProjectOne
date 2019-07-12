class MovieHelper:

    def __init__(self, app):
        self.app = app

    def open_add_movie_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href$='?go=add']").click()

    def create(self, film):
        wd = self.app.wd
        self.open_add_movie_page()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(film.name)
        wd.find_element_by_name("year").clear()
        wd.find_element_by_name("year").send_keys(film.year)
        wd.find_element_by_name("aka").clear()
        wd.find_element_by_name("aka").send_keys(film.description)
        wd.find_element_by_id("submit").click()
        self.return_to_main_page()

    def return_to_main_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("#wrapper > header > div > nav > ul > li:nth-child(1) > a").click()
