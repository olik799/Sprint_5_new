from config import URL
from locators import StellarLocators

class TestStellarBurgers:

    def tests_constructor(self, driver): # переходы по разделам конструктора
        driver.get(URL)

        driver.find_element(*StellarLocators.SAUCE_BUTTON).click()
        driver.find_element(*StellarLocators.SAUCE_HEADER)

        driver.find_element(*StellarLocators.TOPPING_BUTTON).click()
        driver.find_element(*StellarLocators.TOPPING_HEADER)

        driver.find_element(*StellarLocators.BREAD_BUTTON).click()
        driver.find_element(*StellarLocators.BREAD_HEADER)
