from selenium.webdriver.support.ui import Select


#def edit_location(driver):
    # editLocation = driver.find_element_by_id("editLocation").click()
    # catsmo = driver.find_element_by_xpath("//*[@id='selectCode']/option[189]").click()

def edit_location(driver, lat="0", long = "0"):
    driver.find_element_by_id("editLocation").click()
    if lat==0:
        driver.find_element_by_id("lat").clear()
    else:
        driver.find_element_by_id("lat").send_keys(lat)
    if long == 0:
        driver.find_element_by_id("longitude").clear()
    else:
        driver.find_element_by_id("longitude").send_keys(long)
    driver.find_element_by_id("setGPSbutton").click()
def edit_metadata(driver, assign_to_user = ""):
    driver.find_element_by_id("editMeta").click()
    select = Select(driver.find_element_by_id("submitterSelect"))
    select.select_by_visible_text(assign_to_user)
    #driver.find_element_by_id("Assign").click()

def edit_atribute(driver): #we edit the lynx and we select that its Lynux Pardinus
    driver.find_element_by_xpath("//*[@id='editObservation']").click()
    driver.find_element_by_xpath("//*[@id='genusSpecies']/option[2]").click()
    driver.find_element_by_xpath("//*[@id='taxBtn']").click()

def clear_date(driver):
    driver.find_element_by_xpath("//*[@id='editDate']").click()
    driver.find_element_by_xpath("//*[@id='datepickerField']").clear()
    driver.find_element_by_xpath("//*[@id='addResetDate']").click()

def remove_ocurrence(driver):
    driver.find_element_by_xpath("//*[@id='editIdentity']").click()
    try:
        driver.find_element_by_xpath("//*[@id='removeOccurrenceBtn']").click()
    except:
        pass