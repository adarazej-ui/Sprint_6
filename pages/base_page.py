import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу по URL: {url}")
    def navigate_to(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL-адрес страницы")
    def get_current_url(self):

        return self.driver.current_url

    @allure.step("Ожидать видимости элемента {locator}")
    def wait_for_visibility(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидать кликабельности элемента {locator}")
    def wait_for_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидать присутствия элемента в DOM {locator}")
    def wait_for_presence(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Скроллить до элемента и кликнуть через JavaScript")
    def scroll_and_js_click(self, locator):
        element = self.wait_for_presence(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Кликнуть по элементу {locator}")
    def click_element(self, locator):
        self.wait_for_clickable(locator).click()

    @allure.step("Ввести текст в элемент {locator}")
    def send_keys_to_element(self, locator, text):
        element = self.wait_for_visibility(locator)
        element.send_keys(text)

    @allure.step("Отправить специальную клавишу в элемент {locator}")
    def send_special_key(self, locator, key):
        element = self.wait_for_visibility(locator)
        element.send_keys(key)

    @allure.step("Переключиться на последнюю открытую вкладку браузера")
    def switch_to_new_tab(self):
        WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидать, пока URL будет содержать текст: {text}")
    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

