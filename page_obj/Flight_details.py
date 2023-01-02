from selenium.webdriver.common.by import By


class Flight_details:
    def __init__(self, driver):
        self.driver = driver

        self.driver.execute_script("window.scrollTo(0,400)")
        # self.driver.switch_to.window(self.driver.window_handles[1])

    containers = (By.CSS_SELECTOR, ".listingCard")
    view_price = (By.XPATH, "(//span[@class='customArrow arrowDown'])[1]")
    book_now = (By.XPATH,"(//button[@id='bookbutton-RKEY:325f037f-9691-4fb9-a8b6-d089bd87a7aa:14_0'])")

    def get_flight_details(self, index):
        flight_details = {}
        c_index = self.driver.find_elements(*Flight_details.containers)
        title = c_index[index].find_element(By.CSS_SELECTOR, "p.airlineName")
        title_text = title.text
        flight_details['title'] = title_text

        total_duration = c_index[index].find_element(By.CSS_SELECTOR, ".stop-info")
        f_duration = total_duration.text
        flight_details['total_duration'] = f_duration

        arr_time = c_index[index].find_element(By.XPATH, "//div[@class='flexOne timeInfoLeft']//p//span")
        f_arr_time = arr_time.text
        flight_details['arr_time'] = f_arr_time

        dep_time = c_index[index].find_element(By.XPATH, "//div[@class='flexOne timeInfoRight']//p//span")
        f_dep_time = dep_time.text
        flight_details['dep_time'] = f_dep_time

        price = c_index[index].find_element(By.CSS_SELECTOR, "div.priceSection p")
        f_price = price.text
        price_tag = f_price.replace("₹", "")
        # print(price_tag)
        flight_details['price'] = price_tag

        print(flight_details)
        return flight_details

    def get_total_container(self):
        con = self.driver.find_elements(By.CSS_SELECTOR, ".listingCard")
        return len(con)

    def get_price_list(self):
        khalilist = []
        f_fare = self.driver.find_elements(By.CSS_SELECTOR, "div.priceSection p")
        for i in f_fare:
            fare_tag = i.text
            tag_fare = fare_tag.replace("₹", " ")
            # print(tag_fare)
            # p=min(tag_fare)
            khalilist.append(tag_fare)
        khalilist = [int(''.join(x.strip().split(','))) for x in khalilist]
        print("----------------->>>>> hello <<<<<<--------------------")
        print(min(khalilist))

        # breakpoint()
        # khalilist.sort()
        # p = khalilist[0]

        # print(p)
        # x = self.driver.find_element(("))
        # y =xBy.XPATH, "(//span[@class='appendRight8'][normalize-space()='View Prices'])
        obj = khalilist.index(min(khalilist))
        print(obj)

        # view_price_click = khalilist[obj].find_element(By.XPATH, "(//span[@class='appendRight8'][normalize-space()='View Prices'])")
        # view_price_click.click()
        # print(obj)

    def get_view_price(self):
        return self.driver.find_element(*Flight_details.view_price)

    def get_book_now(self):
        book_now_list= self.driver.find_elements(*Flight_details.book_now)
        for books_now_lists in book_now_list:
            return books_now_lists .click()
