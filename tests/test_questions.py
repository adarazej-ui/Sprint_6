import pytest
import allure
from pages.main_page import MainPage
from data import ScooterTestData

class TestScooterQuestions:

    @allure.title("Проверка выпадающего списка в разделе 'Вопросы о важном'")
    @pytest.mark.parametrize(
        "index, expected_text",
        ScooterTestData.ACCORDION_ANSWERS
    )
    
    def test_accordion_questions_and_answers(self, driver, index, expected_text):
        main_page = MainPage(driver)
        main_page.open()
        
        main_page.click_question(index)
        actual_text = main_page.get_answer_text(index)
        
        assert expected_text in actual_text
