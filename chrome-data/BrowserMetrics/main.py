from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pickle
import pandas as pd

#My modules, functions and methods
import login
from navigate import *
from editlynx import *

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#driver.get("https://lynx.wildbook.org/encounters/encounterSearch.jsp")

#login
# link = "https://lynx.wildbook.org/encounters/encounterSearch.jsp"
#link = "https://lynx.wildbook.org/encounters/searchResults.jsp?male=male&female=female&unknown=unknown&alive=alive&dead=dead&numSearchedObs=1&lifeStageField=None&label0=None&numResights=1&biomeasurement13C%28operator%29=gteq&biomeasurement15N%28operator%29=gteq&biomeasurement34S%28operator%29=gteq&state=approved&organizationId=None&projectId=None&submitSearch=Search+Sightings"
#link = "https://lynx.wildbook.org/encounters/encounter.jsp?number=a720ce40-3e86-4a31-95d8-be136bf64c5a"
#link = "https://lynx.wildbook.org/encounters/searchResults.jsp?locationCodeField=CATSMO&male=male&female=female&unknown=unknown&alive=alive&dead=dead&numSearchedObs=1&lifeStageField=None&label0=None&numResights=1&biomeasurement13C%28operator%29=gteq&biomeasurement15N%28operator%29=gteq&biomeasurement34S%28operator%29=gteq&organizationId=None&projectId=None&submitSearch=Search+Sightings"
# link = "https://lynx.wildbook.org/login.jsp"
# login.login(driver, "YOUR USER", "PASSWORD", link)



# location_filter_text(driver, "CATSMO")
# driver.find_element_by_id("submitSearch").click()  # click in submit search
# open_elements_table(driver)
# edit_atribute(driver)
# clear_date(driver)
# remove_ocurrence(driver)
# open_elements_table(driver)

#####login using the specified User and the password
#login.login(driver, "YOURUSER", "PASSWORD", link) #we login and go directly to the link = encounter Seacrh
#####Navigate and filter in Search Encounters
#location_filter_text(driver, "CATSMO") #Location filter text by Location ID
#location_filter_map(driver, 15,15,-15,-15) #Location filter map by coordenates

#searchfield = driver.find_element_by_id("submitSearch").click() #click in submit search

#open_elements_table(driver)



# countTotal = driver.find_element_by_xpath("//*[@id='results-slider']/span").get_attribute("style")

# gets the table
# driver.implicitly_wait(5)
# table = driver.find_element_by_xpath("//*[@id='results-table']") #we create the iterable 'table' with the elements of the table
# tablep = driver.find_element_by_xpath("//*[@id='results-slider']/span").get_attribute("style")
#
# while tablep != "bottom: 0%;":
#     for row in table.find_elements_by_xpath(".//tr")[1:]:
#         row.click() # we open the first elements of the table max 10
#     allTabs = driver.window_handles #save all the tabs in allTABS
#     for tab in allTabs:  # We move tab by tab
#         driver.switch_to.window(tab)
#         try:
#             driver.find_element_by_class_name("pageableTable-wrapper")  # if it is the main tab we do not execute
#         except:
#             driver.implicitly_wait(2)
# #             editLocation = driver.find_element_by_id("editLocation").click()
# #             #catsmo = driver.find_element_by_xpath("//*[@id='selectCode']/option[189]").click()
# #             #canandujar = driver.find_element_by_xpath("// *[ @ id = 'selectCode'] / option[188]").click()
#
#             latitude = driver.find_element_by_id("lat").clear()
#             longitude = driver.find_element_by_id("longitude").clear()
#             setGPSbutton = driver.find_element_by_id("setGPSbutton").click()
#             #editMeta = driver.find_element_by_id("editMeta").click()
#             #catsmo_val = driver.find_element_by_xpath("//*[@id='submitterSelect']/option[8]").click()
#             #catandujar_val = driver.find_element_by_xpath("//*[@id='submitterSelect']/option[7]").click()
#
#             #Assign = driver.find_element_by_id("Assign").click()
#             driver.close()
#     allTabs = driver.window_handles
#     driver.switch_to.window(allTabs[0])
#     driver.find_element_by_class_name("pageableTable-wrapper")
#     for i in range(5): driver.find_element_by_xpath("//*[@id='results-slider']/span").send_keys(Keys.ARROW_DOWN)
#     table = driver.find_element_by_xpath("//*[@id='results-table']")
#     tablep = driver.find_element_by_xpath("//*[@id='results-slider']/span").get_attribute("style")
# else:
#     for row in table.find_elements_by_xpath(".//tr")[1:]:
#         row.click() # we open the first elements of the table max 10
#     allTabs = driver.window_handles #save all the tabs in allTABS
#     for tab in allTabs:  # We move tab by tab
#         driver.switch_to.window(tab)
#         try:
#             driver.find_element_by_class_name("pageableTable-wrapper")  # if it is the main tab we do not execute
#         except:
#             driver.implicitly_wait(2)
#             editLocation = driver.find_element_by_id("editLocation").click()
#             #catsmo = driver.find_element_by_xpath("//*[@id='selectCode']/option[189]").click()
#             #canandujar = driver.find_element_by_xpath("// *[ @ id = 'selectCode'] / option[188]").click()
#
#             latitude = driver.find_element_by_id("lat").clear()
#             longitude = driver.find_element_by_id("longitude").clear()
#             setGPSbutton = driver.find_element_by_id("setGPSbutton").click()
#             #editMeta = driver.find_element_by_id("editMeta").click()
#             #catsmo_val = driver.find_element_by_xpath("//*[@id='submitterSelect']/option[8]").click()
#             #catandujar_val = driver.find_element_by_xpath("//*[@id='submitterSelect']/option[7]").click()
#
#             #Assign = driver.find_element_by_id("Assign").click()
#             driver.close()
#     allTabs = driver.window_handles
#     driver.switch_to.window(allTabs[0])
#     driver.find_element_by_class_name("pageableTable-wrapper")
#     for i in range(5): driver.find_element_by_xpath("//*[@id='results-slider']/span").send_keys(Keys.ARROW_DOWN)
#     table = driver.find_element_by_xpath("//*[@id='results-table']")
#     tablep = driver.find_element_by_xpath("//*[@id='results-slider']/span").get_attribute("style")

print("finished!")


################################################


#TODO ####GETTING COOKIES AND SAVING THEM INTO cookies.txt
# link = "https://lynx.wildbook.org/encounters/encounterSearch.jsp"
# login.login(driver, "YOURUSER", "PASSWORD", link)
# my_cookies = driver.get_cookies()
# print(my_cookies)
# with open('cookies.txt', 'w') as f:
#     print(my_cookies, file=f)

#TODO ## importing cookies into a dict commands
# filename = 'cookies.txt'
# commands = {}
# with open(filename) as fh:
#     for line in fh:
#         command, description = line.strip().split(' ', 1)
#         commands[command] = description.strip()
#driver.get("https://www.google.com/")
#######driver.add_cookie(commands) no funciona :(


# print(driver.current_url)
# print(type(driver.current_url))
'''
try:
    driver.find_element_by_css_selector(".image-enhancer-wrapper").is_displayed()
except:
    print("not found")
'''


# df = pd.read_csv("EncuentrosKowa09.csv")
# print(df.head())
# my_link = "https://lynx.wildbook.org/encounters/encounter.jsp?number="
# pictures_column = []
# for catalognumber in df["catalogNumber"]:
#     catalog_link = my_link + str(catalognumber)
#     driver.get(catalog_link)
#     try:
#         driver.find_element_by_css_selector(".image-enhancer-wrapper").is_displayed()
#         pictures_column.append('Yes')
#     except:
#         pictures_column.append('No')
# df['Picture'] = pictures_column
#
# df.to_csv("file_name09.csv")
#
# driver.quit()
# print("FINISHED!")


# import pandas as pd
# df = pd.read_csv (r'TESTING2.csv')
# df.to_json (r'jsonTESTING2.json')

