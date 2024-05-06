from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import URL
from locators import StellarLocators
from data import name, email_random, password

class TestStellarBurgersRegistration:

    def tests_registtation_new_user(self, driver): # регистрация нового пользователя
        driver.get(f'{URL}register')
        driver.find_element(*StellarLocators.NAME_FIELD).send_keys(name)
        driver.find_element(*StellarLocators.EMAIL_FIELD).send_keys(email_random)
        driver.find_element(*StellarLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarLocators.INPUT_HEADER))
        assert driver.current_url == f'{URL}login'

    def tests_log_in(self, driver): # проверка данных регистрации
        driver.get(f'{URL}login')
        driver.find_element(*StellarLocators.EMAIL_FIELD).send_keys(email_random)
        driver.find_element(*StellarLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*StellarLocators.INPUT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.ORDER_BUTTON))
        assert driver.current_url == URL

    def tests_invalid_password(self, driver): # проверка ошибки некорректного пароля
        driver.get(f'{URL}login')
        driver.find_element(*StellarLocators.EMAIL_FIELD).send_keys(email_random)
        driver.find_element(*StellarLocators.PASSWORD_FIELD).send_keys('111')
        driver.find_element(*StellarLocators.INPUT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.
                                                                                          INVALID_PASSWORD))
        assert driver.find_element(*StellarLocators.INVALID_PASSWORD).text == 'Некорректный пароль'
