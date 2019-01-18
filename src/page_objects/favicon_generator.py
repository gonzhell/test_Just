from src.page_objects.main_page import MainPage


class FaviconGenerator(MainPage):
    generate_favicon_button = '//button[@id="generate_favicon_button"]'

    def __init__(self, driver):
        super().__init__(driver)

    def generate_favicon(self):
        self.driver_helper.wait_element_and_click(self.generate_favicon_button)


'''Here will be some methods to modify settings of creating favicon'''
