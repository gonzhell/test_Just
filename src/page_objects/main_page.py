import logging
import os

from src.helpers.driver_helper import DriverHelper
logging.basicConfig(level=logging.INFO)


class MainPage:
    base_page = 'https://realfavicongenerator.net/'
    select_picture = '//button[@id="select_favicon_picture_button"]'
    input_picture = '//form[@id="favicon_uploader_form"]/div/input'
    generate_favicon = '//button[@id="generate_favicon_button"]'
    invalid_header = '//h4[text()="Your favicon is not correct"]'
    modal_close = '//button[@id="modal_close"]'
    continue_modal = '//button[@id="warning_modal_continue"]'

    def __init__(self, driver):
        self.driver = driver
        self.driver_helper = DriverHelper(driver)

    def open_base_page(self):
        self.driver.get(self.base_page)

    def add_image(self, file):
        self.driver_helper.wait_element_and_send_keys(self.input_picture, os.getcwd() + file)

    def close_invalid_modal(self):
        self.driver_helper.wait_element_and_click(self.modal_close)

    def is_invalid_modal_appears(self):
        return self.driver_helper.displayed(self.invalid_header)

    def is_continue_modal_appears(self):
        return self.driver_helper.displayed(self.continue_modal)

    def continue_modal_apply(self):
        self.driver_helper.wait_element_and_click(self.continue_modal)




