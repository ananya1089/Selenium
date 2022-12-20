from pprint import pprint

from selenium.webdriver.common.by import By

from page_obj.Flight_details import Flight_details
from page_obj.Home_page import Home_page
from page_obj.search_flights import Search_Flight
from utilities.BaseClass import BaseClass



class Test_Main(BaseClass):
    def test_mmt(self):
        home_page = Home_page(self.driver)
        home_page.get_pop_up().click()
        home_page.get_from_btn().click()
        home_page.get_from_city().send_keys("Kolkata, India")
        home_page.get_input_btn().click()
        home_page.get_to_btn().click()
        home_page.get_to_input_city_name().send_keys("Pune, India")
        home_page.get_to_city_btn().click()
        search_flight = Search_Flight(self.driver)
        search_flight.get_search_key().click()
        self.element_wait_clickable(search_flight.page_pop_up)
        search_flight.get_page_pop_up().click()
        flight_details = Flight_details(self.driver)
        # flight_name = flight_details.get_list_of_flights()
        listofFlights = self.driver.find_elements(By.XPATH, "//div[@class='makeFlex align-items-center gap-x-10 airline-info-wrapper']")
        f_name=[]
        for flights in listofFlights:
            names=flights.text
            # print(names)
            f_name.append(names)

        arrival_time = self.driver.find_elements(By.XPATH, "//div[@class='flexOne timeInfoLeft']")
        f_arr_time =[]
        for time in arrival_time:
           arr_time = time.text

           f_arr_time.append(arr_time)


        duration = self.driver.find_elements(By.XPATH, "//div[@class='stop-info flexOne']")
        f_duration_time = []
        for f_duration in duration:
           du_time = f_duration.text
           f_duration_time.append(du_time)
        dep_time = self.driver.find_elements(By.XPATH, "//div[@class='flexOne timeInfoRight']")
        f_dep_time = []
        for dept_time in dep_time:
            d_time=dept_time.text
            f_dep_time.append(d_time)

        dic = {"name":f_name,
             "arrival_time":f_arr_time,
             "duration":f_duration_time,
             "dep_time":f_dep_time}
        pprint(dic)











