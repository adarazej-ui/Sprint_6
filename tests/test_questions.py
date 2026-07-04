import pytest
from pages.main_page import MainPage

class TestScooterQuestions:

    @pytest.mark.parametrize(
        "index, expected_text",
        [
            (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.")
        ]
    )
    def test_accordion_questions_and_answers(self, driver, index, expected_text):
        main_page = MainPage(driver)
        main_page.open()
        
        main_page.click_question(index)
        actual_text = main_page.get_answer_text(index)
        
        assert actual_text == expected_text
