from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Pages.loginPage import LoginPage
from Pages.searchEncounterPage import SearchEncounterPage
import HtmlTestRunner
import pandas as pd
from Pages.encounterPage import EncounterPage
from ddt import ddt, data, file_data, idata
import json #to put double quotation

def number_generator():
    df = pd.read_csv("EncuentrosKowaTEST.csv")
    for catalognumber in df["catalogNumber"]:
        yield json.dumps(catalognumber)
@ddt
class PictureTest(unittest.TestCase):
    # df = pd.read_csv("EncuentrosKowaTEST.csv")
    # ids = []
    # for catalognumber in df["catalogNumber"]:
    #     ids.append(catalognumber)
    # #print(type(ids))

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://lynx.wildbook.org/login.jsp")
        cls.driver.find_element_by_name("username").send_keys("userR")
        cls.driver.find_element_by_name("password").send_keys("123456")  # we enter the password
        cls.driver.find_element_by_id("logMeIn").click()

    @file_data('fewEncounters.json')
    def test_has_picture(self, catalognumber):
        driver = self.driver
        print("The catalognumber is: ", catalognumber)
        print(type(catalognumber))
        catalog_link = "https://lynx.wildbook.org/encounters/encounter.jsp?number=" + str(catalognumber)
        driver.get(catalog_link)
        encounter = EncounterPage(driver)
        self.assertTrue(encounter.has_picture())

    @classmethod
    def tearDownClass(cls): #will run after all the tests are completed
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/kowarika/PycharmProjects/wildbookEncounters/Reports"))
