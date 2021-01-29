from Locators.locators import Locators
class EncounterPage():

    def __init__(self, driver):
        self.driver = driver
        self.image_css = Locators.image_css

    def has_picture(self):
        try:
            self.driver.find_element_by_css_selector(self.image_css).is_displayed()
            return True
        except:
            return False

