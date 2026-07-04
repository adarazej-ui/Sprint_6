from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ScooterMainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qa-scooter.praktikum-services.ru/"

    def open(self):
        if self.driver.current_url != self.url:
            self.driver.get(self.url)

    def click_question(self, index):
        question_locator = ScooterMainPageLocators.get_accordion_question(index)
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(question_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def get_answer_text(self, index):
        answer_locator = ScooterMainPageLocators.get_accordion_answer(index)
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(answer_locator))
        return element.text

    def click_top_order_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(ScooterMainPageLocators.TOP_ORDER_BUTTON)).click()

    def click_bottom_order_button(self):
        element = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located(ScooterMainPageLocators.BOTTOM_ORDER_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_scooter_logo(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(ScooterMainPageLocators.SCOOTER_LOGO)).click()

    def click_yandex_logo(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(ScooterMainPageLocators.YANDEX_LOGO)).click()

