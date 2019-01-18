import pytest
import logging

from src.helpers.check_zip import CheckZip
from src.tests.base_class import BaseClass


class TestLoadImages(BaseClass):

    def setup(self):
        self.check = CheckZip()

    def setup_driver(self, browser, is_incognito=False):
        self.get_driver(browser, is_incognito)

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def check_alerts(self, results):
        if results == "fail":
            assert self.main_page.is_invalid_modal_appears(), "There is no alert modal"
            self.main_page.close_invalid_modal()
        elif results == "attention":
            assert self.main_page.is_continue_modal_appears(), "There is no notification modal"
            self.main_page.continue_modal_apply()


    @pytest.mark.policies
    @pytest.mark.parametrize("browser",
                             [
                                 "chrome",
                                 "ff",
                             ])
    @pytest.mark.parametrize("resolution, result",
                             [
                                 ("69_69", "fail"),
                                 ("70_70", "attention"),
                                 ("259_259", "attention"),
                                 ("260_260", "pass"),
                             ])
    @pytest.mark.parametrize("extension",
                             [
                                 "png",
                                 # "giff",
                                 # "jpg",
                                 # "svg"
                             ])
    def test_job_websites(self, browser, resolution, extension, result):
        logging.info("Starting test {} {} {}".format(resolution, extension, result))
        file = "/source/{}.{}".format(resolution, extension)
        self.setup_driver(browser)
        self.main_page.open_base_page()
        self.main_page.add_image(file)
        self.check_alerts(result)
        if not result == "fail":
            self.favicon_generator.generate_favicon()
            url = self.install_favicon.get_download_url()
            assert self.check.check_zip(url), "Image {} doesn't convert to favicon correct".format(file)

