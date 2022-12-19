from selenium.webdriver.common.by import By


class Home_page:
    def __init__(self, driver):
        self.driver = driver

    pop_up = (By.CSS_SELECTOR, ".loginModal.displayBlock.modalLogin.dynHeight.personal")
    from_btn = (By.CSS_SELECTOR, "label[for='fromCity']")
    from_city = (By.CSS_SELECTOR, "input[placeholder='From']")
    input_btn = (By.XPATH, "//p[normalize-space()='Kolkata, India']")
    to_btn = (By.XPATH, "//span[normalize-space()='To']")
    to_input_city_name = (By.CSS_SELECTOR, "input[placeholder='To']")
    to_city_btn = (By.XPATH, "//p[normalize-space()='Pune, India']")

    def get_pop_up(self):
        return self.driver.find_element(*Home_page.pop_up)

    def get_from_btn(self):
        return self.driver.find_element(*Home_page.from_btn)

    def get_from_city(self):
        return self.driver.find_element(*Home_page.from_city)

    def get_input_btn(self):
        return self.driver.find_element(*Home_page.input_btn)

    def get_to_btn(self):
        return self.driver.find_element(*Home_page.to_btn)

    def get_to_input_city_name(self):
        return self.driver.find_element(*Home_page. to_input_city_name)

    def get_to_city_btn(self):
        return self.driver.find_element(*Home_page.to_city_btn)
