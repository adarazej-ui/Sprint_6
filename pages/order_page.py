from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators import ScooterOrderPageLocators

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_first_step(self, name, surname, address, phone):
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(ScooterOrderPageLocators.NAME_INPUT)).send_keys(name)
        self.driver.find_element(*ScooterOrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*ScooterOrderPageLocators.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*ScooterOrderPageLocators.PHONE_INPUT).send_keys(phone)
    
        metro = self.driver.find_element(*ScooterOrderPageLocators.METRO_STATION_INPUT)
        metro.click()
        metro.send_keys(Keys.DOWN)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(ScooterOrderPageLocators.METRO_DROPDOWN_OPTION)).click()

        self.driver.find_element(*ScooterOrderPageLocators.NEXT_BUTTON).click()

    def fill_second_step(self, date, comment, color="black"):
        
        date_field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(ScooterOrderPageLocators.DATE_INPUT))
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)

        self.driver.find_element(*ScooterOrderPageLocators.RENT_TIME_DROPDOWN).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(ScooterOrderPageLocators.RENT_TIME_OPTION_ONE_DAY)).click()

        if color == "black":
            self.driver.find_element(*ScooterOrderPageLocators.COLOR_BLACK_CHECKBOX).click()
        else:
            self.driver.find_element(*ScooterOrderPageLocators.COLOR_GREY_CHECKBOX).click()

        self.driver.find_element(*ScooterOrderPageLocators.COMMENT_INPUT).send_keys(comment)
        self.driver.find_element(*ScooterOrderPageLocators.FINAL_ORDER_BUTTON).click()

    def confirm_order(self):

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(ScooterOrderPageLocators.CONFIRM_YES_BUTTON)).click()

    def is_order_success_popup_displayed(self):
        
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(ScooterOrderPageLocators.SUCCESS_ORDER_HEADER))
        return element.is_displayed()
