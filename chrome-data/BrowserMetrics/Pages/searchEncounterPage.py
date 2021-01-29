from selenium.webdriver.support.ui import Select
from Locators.locators import Locators
class SearchEncounterPage():

    def __init__(self, driver):
        self.driver = driver

        #location filter map
        self.ne_lat_textbox_id = Locators.ne_lat_textbox_id
        self.ne_long_textbox_id = Locators.ne_long_textbox_id
        self.sw_lat_textbox_id = Locators.sw_lat_textbox_id
        self.sw_long_textbox_id = Locators.sw_long_textbox_id
        self.load_markers_button_xpath = Locators.load_markers_button_xpath

        #location_filter_text
        self.location_filter_text_button_xpath = Locators.location_filter_text_button_xpath
        self.location_filter_text_locationid_id = Locators.location_filter_text_locationid_id

        #submit search
        self.search_button_id = "submitSearch"

    def enter_locations_filters_map(self, ne_lat, ne_long, sw_lat, sw_long):
        self.driver.find_element_by_id(self.ne_lat_textbox_id).send_keys(ne_lat)
        self.driver.find_element_by_id(self.ne_long_textbox_id).send_keys(ne_long)
        self.driver.find_element_by_id(self.sw_lat_textbox_id).send_keys(sw_lat)
        self.driver.find_element_by_id(self.sw_long_textbox_id).send_keys(sw_long)

    def click_load_markers(self):
        self.driver.find_element_by_xpath(self.load_markers_button_xpath).click()

    def click_location_filter_text(self):
        self.driver.find_element_by_xpath(self.location_filter_text_button_xpath).click()

    def set_location_filter_text_locationid(self, location_id):
        select = Select(self.driver.find_element_by_id(self.location_filter_text_locationid_id))
        select.select_by_visible_text(location_id)

    def click_search(self):
        self.driver.find_element_by_id(self.search_button_id).click()