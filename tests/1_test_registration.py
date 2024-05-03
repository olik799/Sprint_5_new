import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.config import URL
from tests.locators import StellarLocators

name = 'Olga'
email = f'olgaz5{random.randint(100,999)}@yandex.ru'
password = '1234567'

class TestStellarBurgers:

    def tests_register(self, driver): # регистрация нового пользователя
        driver.get(f'{URL}register')
        driver.find_element(*StellarLocators.NAME_FIELD).send_keys(name)
        driver.find_element(*StellarLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*StellarLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarLocators.INPUT_HEADER))
        assert driver.current_url == f'{URL}login'

    def tests_log_in(self, driver): # проверка данных регистрации
        driver.get(f'{URL}login')
        driver.find_element(*StellarLocators.EMAIL_FIELD_IN).send_keys(email)
        driver.find_element(*StellarLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*StellarLocators.INPUT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.ORDER_BUTTON))
        assert driver.current_url == URL

    def tests_invalid_password(self, driver): # проверка ошибки некорректного пароля
        driver.get(f'{URL}login')
        driver.find_element(*StellarLocators.EMAIL_FIELD_IN).send_keys(email)
        driver.find_element(*StellarLocators.PASSWORD_FIELD).send_keys('111')
        driver.find_element(*StellarLocators.INPUT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.INPUT_HEADER))
        assert driver.current_url == f'{URL}login'
