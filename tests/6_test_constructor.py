from config import URL
from locators import StellarLocators


class TestStellarBurgersConstructor:

    def tests_move_to_section_bread(self, driver):  # переход в раздел 'Булки' из раздела 'Соусы'
        driver.get(URL)
        driver.find_element(*StellarLocators.SAUCE_BUTTON).click()
        driver.find_element(*StellarLocators.BREAD_BUTTON).click()
        assert 'current' in driver.find_element(*StellarLocators.BREAD_BUTTON).get_attribute('class')

    def tests_move_to_section_sauce(self, driver):  # переход в раздел 'Соусы'
        driver.get(URL)
        driver.find_element(*StellarLocators.SAUCE_BUTTON).click()
        assert 'current' in driver.find_element(*StellarLocators.SAUCE_BUTTON).get_attribute('class')

    def tests_move_to_section_topping(self, driver):  # переход в раздел 'Начинки'
        driver.get(URL)
        driver.find_element(*StellarLocators.TOPPING_BUTTON).click()
        assert 'current' in driver.find_element(*StellarLocators.TOPPING_BUTTON).get_attribute('class')
