from selenium import webdriver
import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))

from POMProject.Pages.search_roundtrip import Search_Round_Trip_Page


class Booking_Tickets_TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/Pallavi/Downloads/drivers/chromedriver.exe')

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_roundtrip_tickets(self):
        driver = self.driver
        driver.get("https://www.goibibo.com/")
        Booking = Search_Round_Trip_Page(driver)
        Booking.test_click_round_trip()
        time.sleep(2)
        Booking.test_input_from("Delhi(DEL)")
        time.sleep(2)
        Booking.test_input_destination("Mumbai (BOM)")
        time.sleep(2)
        Booking.test_click_departure_call()
        time.sleep(2)
        Booking.test_depart_date()
        time.sleep(2)
        Booking.test_click_return_call()
        time.sleep(5)
        Booking.test_return_date()
        time.sleep(2)

        Booking.test_search()
        time.sleep(2)




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
