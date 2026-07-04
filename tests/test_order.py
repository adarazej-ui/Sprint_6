import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestScooterOrderFlow:

    @pytest.mark.parametrize(
        "entry_point, name, surname, address, phone, date, comment, color",
        [
            ("top", "Анастасия", "Ратушняк", "ул. Космонавтов, 12", "89991234567", "15.07.2026", "Позвонить за час", "black"),
            ("bottom", "Андрей", "Вилков", "пр. Ленина, 45 кв 3", "89117654321", "20.07.2026", "Оставить у двери", "grey")
        ]
    )
    def test_order_scooter_success_flow(self, driver, entry_point, name, surname, address, phone, date, comment, color):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.open()
        
        if entry_point == "top":
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        order_page.fill_first_step(name, surname, address, phone)
        order_page.fill_second_step(date, comment, color)
        order_page.confirm_order()

        assert order_page.is_order_success_popup_displayed()


class TestScooterLogoNavigation:

    def test_click_scooter_logo_navigates_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_top_order_button()
        
        main_page.click_scooter_logo()
        WebDriverWait(driver, 5).until(lambda d: d.current_url == "https://qa-scooter.praktikum-services.ru/")
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    def test_click_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        
        main_page.click_yandex_logo()
        
        WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])
        
        WebDriverWait(driver, 10).until(lambda d: "dzen" in d.current_url)
        assert "dzen" in driver.current_url

