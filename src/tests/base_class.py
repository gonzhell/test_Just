from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import RemoteConnection

from src.page_objects.Install_favicon import InstallFavicon
from src.page_objects.favicon_generator import FaviconGenerator
from src.page_objects.main_page import MainPage


class BaseClass:
    driver = None
    browser = None
    main_page = None
    favicon_generator = None
    install_favicon = None

    def get_driver(self, browser, is_incognito=False):
        """here is minimum configuration features to create proper browser session"""
        RemoteConnection.set_timeout(10)
        self.browser = browser
        if not self.driver:
            if browser.lower() == 'chrome':
                capa = DesiredCapabilities.CHROME
                capa["pageLoadStrategy"] = "none"
                options = Options()
                if is_incognito:
                    options.add_argument('--incognito')
                options.add_argument('--no-sandbox')
                self.driver = webdriver.Chrome(options=options, desired_capabilities=capa)
            elif browser.lower() == 'ff':
                firefox_profile = webdriver.FirefoxProfile()
                if is_incognito:
                    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
                else:
                    firefox_profile.set_preference("browser.privatebrowsing.autostart", False)
                self.driver = webdriver.Firefox(firefox_profile=firefox_profile)
            """easy extend on other different browsers like IE, EDGE ..."""
        self.main_page = MainPage(self.driver)
        self.favicon_generator = FaviconGenerator(self.driver)
        self.install_favicon = InstallFavicon(self.driver)
        return self.driver

    def restart_driver(self, is_incognito=False):
        if self.driver:
            self.driver.quit()
            self.driver = None
        self.get_driver(self.browser, is_incognito)