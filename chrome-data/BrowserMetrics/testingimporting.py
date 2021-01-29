from selenium.webdriver.support.ui import Select

def location_filter_text(driver, Location_ID):
    driver.find_element_by_xpath("// *[ @ id = 'search'] / table / tbody / tr[2] / td / h4 / a").click()
    select = Select(driver.find_element_by_id("locationCodeField"))
    select.select_by_visible_text(Location_ID)