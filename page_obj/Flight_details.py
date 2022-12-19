from selenium.webdriver.common.by import By


class Flight_details:
    def __init__(self, driver):
        self.driver = driver

    listOfFlights = (By.CSS_SELECTOR, ".makeFlex.simpleow")
    name_of_flights = (By.CSS_SELECTOR, ".airlineName")
    flight_dep_arr = (By.CSS_SELECTOR, ".flightTimeInfo")
    flight_price = (By.CSS_SELECTOR, ".white-space-no-wrap")
    flight_duration = (By.CSS_SELECTOR, ".stop-info")
    flightNumber = (By.CSS_SELECTOR, ".fliCode")

    def get_list_of_flights(self):
        flight_of_index = self.driver.find_elements(*Flight_details.listOfFlights)
        for flights in flight_of_index:
            print(flights.text)

