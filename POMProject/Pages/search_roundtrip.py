class Search_Round_Trip_Page():

    def __init__(self, driver):
        self.driver = driver
        self.click_round_trip_id = "roundTrip"
        self.input_from_id = "gosuggest_inputSrc"
        self.input_destination_id = "gosuggest_inputDest"
        self.depart_call_id = "departureCalendar"
        self.depart_date_id = "fare_20200828"
        self.return_call_id = "returnCalendar"
        self.return_date_id = "fare_20200830"
        self.search_btn_id = "gi_search_btn"



#to click the roundtrip button
    def test_click_round_trip(self):
        self.driver.find_element_by_id(self.click_round_trip_id).click()
# to click on from
    def test_input_from(self,departure):
        self.driver.find_element_by_id(self.input_from_id).clear()
        self.driver.find_element_by_id(self.input_from_id).send_keys(departure)
# to click on destination
    def test_input_destination(self,destination):
        self.driver.find_element_by_id(self.input_destination_id).clear()
        self.driver.find_element_by_id(self.input_destination_id).send_keys(destination)

# to click on departure callender
    def test_click_departure_call(self):
        self.driver.find_element_by_id(self.depart_call_id).click()
# to fill departure date
    def test_depart_date(self):
        #self.driver.find_element_by_id(self.depart_date_id).clear()
        self.driver.find_element_by_id(self.depart_date_id).click()

# to click on return call
    def test_click_return_call(self):
        self.driver.find_element_by_id(self.return_call_id).click()

# to fill return date
    def test_return_date(self):
        #self.driver.find_element_by_id(self.return_date_id).clear()
        self.driver.find_element_by_id(self.return_date_id).click()

    def test_search(self):
        #self.driver.find_element_by_id(self.search_btn_id).clear()
        self.driver.find_element_by_id(self.search_btn_id).click()







