from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from editlynx import *

# class NavigateTo:
#     def __init__(self, driver):
#         self.driver = driver

def location_filter_text(driver, Location_ID):
    driver.find_element_by_xpath("// *[ @ id = 'search'] / table / tbody / tr[2] / td / h4 / a").click()
    select = Select(driver.find_element_by_id("locationCodeField"))
    select.select_by_visible_text(Location_ID)

    #driver.find_element_by_id("submitSearch").click()  # click in submit search

def location_filter_map(driver, ne_lat, ne_long, sw_lat, sw_long):
    driver.find_element_by_id("ne_lat").send_keys(ne_lat)
    driver.find_element_by_id("ne_long").send_keys(ne_long)
    driver.find_element_by_id("sw_lat").send_keys(sw_lat)
    driver.find_element_by_id("sw_long").send_keys(sw_long)
    driver.find_element_by_xpath("//*[@id='map_overlay_buttons']/input").click()

def open_elements_table(driver, assign_to_user = "", lat="0", long = "0"):
    wait = WebDriverWait(driver, 60)
    table = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='results-table']"))) #we create the iterable 'table' with the elements of the table
    tablep = driver.find_element_by_xpath("//*[@id='results-slider']/span").get_attribute("style")
    while tablep != "bottom: 0%;":
        for row in table.find_elements_by_xpath(".//tr")[1:]:
            row.click() # we open the first elements of the table max 10
        allTabs = driver.window_handles #save all the tabs in allTABS
        for tab in allTabs:  # We move tab by tab
            driver.switch_to.window(tab)
            try:
                 driver.find_element_by_class_name("pageableTable-wrapper")  # if it is the main tab we do not execute
                 print("It has picture!")
            except:
                driver.implicitly_wait(3)

                #edit_location(driver, lat, long)
                #edit_metadata(driver, assign_to_user)
                #clear_date(driver)
                driver.close()

        allTabs = driver.window_handles
        driver.switch_to.window(allTabs[0])
        driver.find_element_by_class_name("pageableTable-wrapper")
        for i in range(10): driver.find_element_by_xpath("//*[@id='results-slider']/span").send_keys(Keys.ARROW_DOWN)
        table = driver.find_element_by_xpath("//*[@id='results-table']")
        tablep = driver.find_element_by_xpath("//*[@id='results-slider']/span").get_attribute("style")
    else:
        for row in table.find_elements_by_xpath(".//tr")[1:]:
            row.click()
        allTabs = driver.window_handles  # save all the tabs in allTABS
        for tab in allTabs:  # We move tab by tab
            driver.switch_to.window(tab)
            try:
                driver.find_element_by_class_name(
                    "pageableTable-wrapper")  # if it is the main tab we do not execute
            except:
                driver.implicitly_wait(2)
                clear_date(driver)
                #edit_location(driver, lat, long)
                #edit_metadata(driver, assign_to_user)
                driver.close()
        allTabs = driver.window_handles
        driver.switch_to.window(allTabs[0])
        driver.find_element_by_class_name("pageableTable-wrapper")
        for i in range(5): driver.find_element_by_xpath("//*[@id='results-slider']/span").send_keys(Keys.ARROW_DOWN)
        table = driver.find_element_by_xpath("//*[@id='results-table']")
        tablep = driver.find_element_by_xpath("//*[@id='results-slider']/span").get_attribute("style")


    ##DO SOMETHING WITH THE LYNX

        #editLocation = self.driver.find_element_by_id("editLocation").click()
        #catsmo = driver.find_element_by_xpath("//*[@id='selectCode']/option[189]").click()
        #canandujar = driver.find_element_by_xpath("// *[ @ id = 'selectCode'] / option[188]").click()
