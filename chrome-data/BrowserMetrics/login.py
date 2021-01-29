from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def login(driver, user, password, link = "https://lynx.wildbook.org/encounters/encounterSearch.jsp"):
    driver.get(link)
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))  # we can use By.Name/otherthings
    )
    login.send_keys(user)  # we ender the user
    driver.find_element_by_name("password").send_keys(password)  # we enter the password
    driver.find_element_by_id("logMeIn").click()  # click in login


