import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    
    driver.get("https://qa-scooter.praktikum-services.ru/")
    try:
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        ).click()
    except Exception:
        pass
        
    yield driver
    driver.quit()
