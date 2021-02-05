from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Pages.loginPage import LoginPage
from Pages.searchEncounterPage import SearchEncounterPage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://lynx.wildbook.org/login.jsp")
        login = LoginPage(driver)
        login.enter_username("ENTER_YOUR_USER")
        login.enter_password("ENTER YOUR PASSWORD")
        login.click_login()
        current_url = login.check_url()
        self.assertTrue(current_url == "https://lynx.wildbook.org/welcome.jsp")

    # searchencounter = SearchEncounterPage(driver)
        # searchencounter.click_location_filter_text()
        # searchencounter.set_location_filter_text_locationid("CATSMO")
        # searchencounter.click_search()


        # self.driver.find_element_by_name("username").send_keys("userR")  # we enter the password
        # self.driver.find_element_by_name("password").send_keys("123456")  # we enter the password
        # self.driver.find_element_by_id("logMeIn").click()  # click in login

    @unittest.skip("we are skipping this test")
    def test_login_valid_invalid_user(self):
        driver = self.driver
        driver.get("https://lynx.wildbook.org/login.jsp")
        login = LoginPage(driver)
        login.enter_username("ENTERYOURUSER")
        login.enter_password("PASSWORD")
        login.click_login()
        welcome_url = "https://lynx.wildbook.org/welcome.jsp"
        current_url = login.check_url()
        self.assertEqual(welcome_url, current_url)

        #driver.current_url


    @classmethod
    def tearDownClass(cls): #will run after all the tests are completed
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/kowarika/PycharmProjects/wildbookEncounters/Reports"))
