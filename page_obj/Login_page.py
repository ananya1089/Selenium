from selenium.webdriver.common.by import By


class Login_page:
    def __init__(self, driver):
        self.driver = driver
    login_btn = (By.CSS_SELECTOR, ".bnplBtn")

    def get_login_btn(self):
        return self.driver.find_element(*Login_page.login_btn)