from selenium.webdriver.common.by import By

class ScooterMainPageLocators:
    
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")
    
    # Кнопки заказа
    TOP_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header_Nav') or contains(@class, 'Header_Header')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_ThirdPart') or contains(@class, 'Home_RoadMap')]//button[text()='Заказать']")
    
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")

    # Секция "Вопросы о важном" (сдвинуты строго на 4 пробела)
    @staticmethod
    def get_accordion_question(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def get_accordion_answer(index):
        return (By.ID, f"accordion__panel-{index}")


class ScooterOrderPageLocators:
    
    NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    
    METRO_DROPDOWN_OPTION = (By.XPATH, ".//li[contains(@class, 'select-search__row') or contains(@class, 'select-search__option')]")
    
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME_DROPDOWN = (By.XPATH, ".//div[@class='Dropdown-control']")
    RENT_TIME_OPTION_ONE_DAY = (By.XPATH, ".//div[text()='сутки']")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    FINAL_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    
    CONFIRM_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_ORDER_HEADER = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")