import allure
from pages.base_page import BasePage
from locators import ScooterMainPageLocators
from constants import ScooterUrls

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
        self.url = f"{ScooterUrls.BASE_URL}{ScooterUrls.MAIN_PAGE_ENDPOIND}"

    @allure.step("Открыть главную страницу Яндекс.Самоката")
    def open(self):
        if self.get_current_url() != self.url:
            self.navigate_to(self.url)

    @allure.step("Кликнуть по стрелочке вопроса номер {index}")
    def click_question(self, index):
        question_locator = ScooterMainPageLocators.get_accordion_question(index)
        self.scroll_and_js_click(question_locator)

    @allure.step("Получить текст ответа для вопроса номер {index}")
    def get_answer_text(self, index):
        answer_locator = ScooterMainPageLocators.get_accordion_answer(index)
        element = self.wait_for_visibility(answer_locator)
        return element.text

    @allure.step("Кликнуть по верхней кнопке 'Заказать'")
    def click_top_order_button(self):
        self.click_element(ScooterMainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Кликнуть по нижней кнопке 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_and_js_click(ScooterMainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Кликнуть по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click_element(ScooterMainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.click_element(ScooterMainPageLocators.YANDEX_LOGO)

