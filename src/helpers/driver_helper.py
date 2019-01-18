from selenium.common import exceptions
from time import sleep
import logging
logging.basicConfig(level=logging.INFO)


class DriverHelper:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_xpath(self, selector, retries=25):
        ret = retries
        not_visible = False
        while retries:
            try:
                element = self.driver.find_element_by_xpath(selector)
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                if element.is_displayed():
                    return element
                else:
                    not_visible = True
                    sleep(1)
                    retries -= 1

            except (
                    exceptions.ElementNotVisibleException,
                    exceptions.WebDriverException,
                    exceptions.ElementNotInteractableException,
                    ):
                if retries <= 0:
                    raise
                else:
                    retries -= 1
                    sleep(1)
        if not_visible:
            logging.info("Try to click on invisible element")
            return element

        raise exceptions.ElementNotVisibleException(
            "Element not visible despite waiting for %s seconds %s" % (selector, ret)
        )

    def wait_element_and_scroll(self, selector):
        element = self.wait_element_xpath(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def wait_element_and_click(self, selector, retries=3):
        while retries:
            try:
                return self.wait_element_xpath(selector).click()
            except exceptions.StaleElementReferenceException:
                if retries <= 0:
                    raise
                else:
                    pass
                retries -= 1
                sleep(1)

    def wait_element_and_send_keys(self, selector, keys):
        self.wait_element_xpath(selector).send_keys(keys)

    def displayed(self, selector):
        try:
            self.driver.find_element_by_xpath(selector).is_displayed()
            return True
        except:
            return False