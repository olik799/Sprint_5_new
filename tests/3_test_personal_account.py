from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import URL
from locators import StellarLocators

email = 'olgaz57777@yandex.ru'
password = '1234567'

class TestStellarBurgers:

    def tests_personal_account_input(self, driver): # вход в аккаунт и переход в личный кабинет
        driver.get(f'{URL}login')
        driver.find_element(*StellarLocators.EMAIL_FIELD_IN).send_keys(email)
        driver.find_element(*StellarLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*StellarLocators.INPUT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.BREAD_HEADER))
        driver.find_element(*StellarLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.EXIT_BUTTON))

        assert driver.current_url == f'{URL}account/profile'
