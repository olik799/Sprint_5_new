from selenium.webdriver.common.by import By

class StellarLocators:
    NAME_FIELD = (By.XPATH, "//form/fieldset[1]/div/div/input") # форма регистрации поле Имя
    EMAIL_FIELD = (By.XPATH, "//form/fieldset[2]/div/div/input") # форма регистрации поле email
    PASSWORD_FIELD = (By.NAME, "Пароль") # форма регистрации поле Пароль
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # форма регистрации кнопка Зарегистрироваться

    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # кнопка оформить заказ

    LOG_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # кнопка Войти в аккаунт
    INPUT_BUTTON = (By.XPATH, "//button[text()='Войти']") # кнопка Войти - форма ввода email и пароль
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") # кнопка Личный Кабинет

    INPUT_BUTTON_REGISTRATION_FORM = (By.XPATH, "//a[text()='Войти']") # кнопка Войти в форме регистрации

# Вход в личный кабинет
    INPUT_HEADER = (By.XPATH, "//h2[text()='Вход']") # заголовок Вход
    EMAIL_FIELD_IN = (By.XPATH, "//form/fieldset[1]/div/div/input")  # вход поле email
    INVALID_PASSWORD = ((By.XPATH, "//p[contains(@class, 'input__error')]")) # сообщение некорректный пароль

# Выход из аккаунта
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']") # кнопка Выход в личном кабинете

# Раздел Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # конструктор
    STELLAR_LOGO = (By.XPATH, "//div[contains(@class, 'logo')]") # логотип

    BREAD_BUTTON = (By.XPATH, "//main/section[1]/div[1]/div[1]") # конструктор Булки
    BREAD_HEADER = (By.XPATH, "//h2[text()='Булки']") # раздел Булки

    SAUCE_BUTTON = (By.XPATH, "//main/section[1]/div[1]/div[2]") # конструктор Соусы
    SAUCE_HEADER = (By.XPATH, "//h2[text()='Соусы']") # раздел Соусы

    TOPPING_BUTTON = (By.XPATH, "//main/section[1]/div[1]/div[3]") # конструктор Начинки
    TOPPING_HEADER = (By.XPATH, "//h2[text()='Начинки']") # раздел Начинки
