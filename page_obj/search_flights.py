from selenium.webdriver.common.by import By


class Search_Flight:
    def __init__(self, driver):
        self.driver = driver

    search_key = (By.CSS_SELECTOR, ".primaryBtn.font24.latoBold.widgetSearchBtn")
    page_pop_up = (By.CSS_SELECTOR, ".bgProperties.icon20.overlayCrossIcon")

    def get_search_key(self):
        return self.driver.find_element(*Search_Flight.search_key)

    def get_page_pop_up(self):
        return self.driver.find_element(*Search_Flight.page_pop_up)