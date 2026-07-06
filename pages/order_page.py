import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators import ScooterOrderPageLocators

class OrderPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнить форму 'Для кого самокат': {name} {surname}")
    def fill_first_step(self, name, surname, address, phone):
        self.send_keys_to_element(ScooterOrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_element(ScooterOrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys_to_element(ScooterOrderPageLocators.ADDRESS_INPUT, address)
        self.send_keys_to_element(ScooterOrderPageLocators.PHONE_INPUT, phone)
        
        metro_field = self.wait_for_clickable(ScooterOrderPageLocators.METRO_STATION_INPUT)
        metro_field.click()
    
        self.send_special_key(ScooterOrderPageLocators.METRO_STATION_INPUT, Keys.DOWN)
        
        self.wait_for_visibility(ScooterOrderPageLocators.METRO_DROPDOWN_OPTION, timeout=5)
        
        self.click_element(ScooterOrderPageLocators.METRO_DROPDOWN_OPTION)
        
        self.click_element(ScooterOrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму 'Про аренду': дата {date}, цвет {color}")
    def fill_second_step(self, date, comment, color="black"):
        date_field = self.wait_for_visibility(ScooterOrderPageLocators.DATE_INPUT)
        date_field.send_keys(date)
        self.send_special_key(ScooterOrderPageLocators.DATE_INPUT, Keys.ENTER)
        self.click_element(ScooterOrderPageLocators.RENT_TIME_DROPDOWN)
        self.click_element(ScooterOrderPageLocators.RENT_TIME_OPTION_ONE_DAY)
        if color == "black":
            self.click_element(ScooterOrderPageLocators.COLOR_BLACK_CHECKBOX)
        else:
            self.click_element(ScooterOrderPageLocators.COLOR_GREY_CHECKBOX)
        self.send_keys_to_element(ScooterOrderPageLocators.COMMENT_INPUT, comment)
        self.click_element(ScooterOrderPageLocators.FINAL_ORDER_BUTTON)

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        self.click_element(ScooterOrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Проверить появление всплывающего окна 'Заказ оформлен'")
    def is_order_success_popup_displayed(self):
        element = self.wait_for_visibility(ScooterOrderPageLocators.SUCCESS_ORDER_HEADER)
        return element.is_displayed()
