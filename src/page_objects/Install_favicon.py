from src.page_objects.main_page import MainPage


class InstallFavicon(MainPage):
    download_results = '//span[@class="favicon_package"]/a'

    def __init__(self, driver):
        super().__init__(driver)

    def get_download_url(self):
        self.driver_helper.wait_element_and_click(self.download_results)

    """Here will be some methods to working with final page. 
    download, install, check ..."""
