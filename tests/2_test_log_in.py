from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.config import URL
from tests.locators import StellarLocators

class TestStellarBurgers:

    def tests_log_in_account_button(self, driver): # вход через кнопку "Войти в аккаунт" на главной
        driver.get(URL)
        driver.find_element(*StellarLocators.LOG_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.INPUT_HEADER))
        assert driver.current_url == f'{URL}login'

    def tests_log_in_personal_account_button(self, driver): # вход через кнопку "Личный кабинет"
        driver.get(URL)
        driver.find_element(*StellarLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.INPUT_HEADER))
        assert driver.current_url == f'{URL}login'

    def tests_lod_in_register_form(self, driver): # вход через кнопку "Войти" в форме регистрации
        driver.get(f'{URL}register')
        driver.find_element(*StellarLocators.INPUT_BUTTON_REGISTRATION_FORM).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.INPUT_HEADER))
        assert driver.current_url == f'{URL}login'

    def tests_lod_in_forgot_password(self, driver): # вход через кнопку "Войти" в форме восстановления пароля
        driver.get(f'{URL}forgot-password')
        driver.find_element(*StellarLocators.INPUT_BUTTON_REGISTRATION_FORM).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.INPUT_HEADER))
        assert driver.current_url == f'{URL}login'
