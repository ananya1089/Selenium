import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass:
    def element_wait_clickable(self, path, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.element_to_be_clickable(path))

