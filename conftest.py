import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import ScooterUrls
from locators import ScooterMainPageLocators

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()

    driver.get(ScooterUrls.BASE_URL)
   
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(ScooterMainPageLocators.COOKIE_ACCEPT_BUTTON)
        ).click()
    except Exception:
        pass
        
    yield driver
    driver.quit()
