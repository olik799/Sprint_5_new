from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import URL
from locators import StellarLocators

class TestStellarBurgersSwitchToLogInPage:

    def tests_click_account_button(self, driver): # через кнопку "Войти в аккаунт" на главной
        driver.get(URL)
        driver.find_element(*StellarLocators.LOG_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.INPUT_HEADER))
        assert driver.current_url == f'{URL}login'

    def tests_click_personal_account_button(self, driver): # через кнопку "Личный кабинет"
        driver.get(URL)
        driver.find_element(*StellarLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.INPUT_HEADER))
        assert driver.current_url == f'{URL}login'

    def tests_click_enter_button_from_register_form(self, driver): # через кнопку "Войти" в форме регистрации
        driver.get(f'{URL}register')
        driver.find_element(*StellarLocators.INPUT_BUTTON_REGISTRATION_FORM).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.INPUT_HEADER))
        assert driver.current_url == f'{URL}login'

    def tests_click_enter_button_in_forgot_password_form(self, driver): # через кнопку "Войти" в форме восстановления пароля
        driver.get(f'{URL}forgot-password')
        driver.find_element(*StellarLocators.INPUT_BUTTON_REGISTRATION_FORM).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarLocators.INPUT_HEADER))
        assert driver.current_url == f'{URL}login'
