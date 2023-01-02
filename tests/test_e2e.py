import time

from page_obj.Flight_details import Flight_details
from page_obj.Home_page import Home_page
from page_obj.Login_page import Login_page

from page_obj.search_flights import Search_Flight

from utilities.BaseClass import BaseClass


class Test_Main(BaseClass):
    def test_mmt(self):
        home_page = Home_page(self.driver)
        home_page.get_pop_up().click()
        home_page.get_radio_btn().click()
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
        flight_details.get_flight_details(index=0)

        flight_list = []
        total_container = flight_details.get_total_container()
        for i in range(total_container):
            flight_list.append(flight_details.get_flight_details(i))
        print(len(flight_list))
        print(flight_list)
        print(flight_list[0]['price'])
        flight_details.get_price_list()
        # flight_details.get_view_price()
        flight_details.get_view_price().click()

        # self.element_wait_clickable(flight_details.book_now)

        flight_details.get_book_now()
        # self.prsence_of_element(flight_details.book_now)
        self.driver.switch_to.window(self.driver.window_handles[0])
        login_page = Login_page(self.driver)

        self.prsence_of_element(login_page.login_btn)
        login_page.get_login_btn().click()
        time.sleep(10)




