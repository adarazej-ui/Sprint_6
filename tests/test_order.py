import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ScooterTestData

class TestScooterOrderFlow:

    @allure.title("Успешное оформление заказа самоката через верхнюю кнопку 'Заказать'")
    @pytest.mark.parametrize(
        "name, surname, address, phone, date, comment, color",
        [ScooterTestData.ORDER_DATA_1]
    )
    def test_order_scooter_via_top_button_success(self, driver, name, surname, address, phone, date, comment, color):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.open()
        main_page.click_top_order_button()
        order_page.fill_first_step(name, surname, address, phone)
        order_page.fill_second_step(date, comment, color)
        order_page.confirm_order()

        assert order_page.is_order_success_popup_displayed()

    @allure.title("Успешное оформление заказа самоката через нижнюю кнопку 'Заказать'")
    @pytest.mark.parametrize(
        "name, surname, address, phone, date, comment, color",
        [ScooterTestData.ORDER_DATA_2]
    )
    def test_order_scooter_via_bottom_button_success(self, driver, name, surname, address, phone, date, comment, color):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open()
        main_page.click_bottom_order_button()
        order_page.fill_first_step(name, surname, address, phone)
        order_page.fill_second_step(date, comment, color)
        order_page.confirm_order()
        assert order_page.is_order_success_popup_displayed()

class TestScooterLogoNavigation:

    @allure.title("Проверка клика по логотипу 'Самокат': переход на главную страницу")
    def test_click_scooter_logo_navigates_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_top_order_button()
        
        main_page.click_scooter_logo()
        main_page.wait_for_url_contains(main_page.url)
        assert main_page.get_current_url() == main_page.url

    @allure.title("Проверка клика по логотипу 'Яндекс': редирект на Дзен в новой вкладке")
    def test_click_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        
        main_page.click_yandex_logo()
        
        main_page.switch_to_new_tab()
        main_page.wait_for_url_contains("dzen")
        
        assert "dzen" in main_page.get_current_url()

