from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument('no-sandbox')
driver = webdriver.Chrome(PATH,options=chrome_options)
driver.get('https://lynx.wildbook.org/encounters/encounterSearch.jsp')  # Already authenticated
time.sleep(30)

driver.get('https://lynx.wildbook.org/encounters/encounterSearch.jsp')
#chrome_options.add_argument("user-data-dir=chrome-data")
 # Time to enter credentials

