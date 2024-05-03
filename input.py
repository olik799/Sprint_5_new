import random

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")


driver.find_element(By.XPATH, ".//button[text() = 'Личный Кабинет']").click()

driver.find_element(By.XPATH, ".//button[text() = 'Зарегистрироваться']").click()


# Регистрация
driver.find_element(By.ID, "name").send_keys("Olga")
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()


driver.quit()
