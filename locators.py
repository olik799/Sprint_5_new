from selenium.webdriver.common.by import By

class StellarLocators:
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following::input")  # форма регистрации поле Имя
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following::input")  # форма регистрации поле email
    PASSWORD_FIELD = (By.NAME, "Пароль") # форма регистрации поле Пароль
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # форма регистрации кнопка Зарегистрироваться

    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # кнопка оформить заказ

    LOG_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # кнопка Войти в аккаунт
    INPUT_BUTTON = (By.XPATH, "//button[text()='Войти']") # кнопка Войти - форма ввода email и пароль
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") # кнопка Личный Кабинет

    INPUT_BUTTON_REGISTRATION_FORM = (By.XPATH, "//a[text()='Войти']") # кнопка Войти в форме регистрации

# Вход в личный кабинет
    INPUT_HEADER = (By.XPATH, "//h2[text()='Вход']") # заголовок Вход
    INVALID_PASSWORD = ((By.XPATH, "//p[contains(@class, 'input__error')]")) # сообщение некорректный пароль

# Выход из аккаунта
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']") # кнопка Выход в личном кабинете

# Раздел Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # конструктор
    STELLAR_LOGO = (By.XPATH, "//div[contains(@class, 'logo')]") # логотип
    MAKE_BURGER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")  # конструктор Булки

    BREAD_BUTTON = (By.XPATH, "//span[text()='Булки']/parent::div") # конструктор Булки
    SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']/parent::div") # конструктор Соусы
    TOPPING_BUTTON = (By.XPATH, "//span[text()='Начинки']/parent::div") # конструктор Начинки
