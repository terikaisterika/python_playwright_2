from app_structure.components.base_component import BaseComponent
from playwright.sync_api import Page
from app_structure.elements.input import Input
from app_structure.elements.button import Button
import allure


class Header(BaseComponent):
    def __init__(self, page: Page):
        self.name = "header компонент"
        super().__init__(page)
        self.search_input = Input(
            page, "input#filter_keyword", "поле поиска 'Search Keywords'"
        )
        self.search_button = Button(
            page, "form#search_form i", "кнопка в поле 'Search Keywords'"
        )

    def find_product(self, phrase: str) -> str:
        step_description = f"Поиск товара по фразе '{phrase}'"
        with allure.step(step_description):
            self.search_input.fill(phrase)
            self.search_button.click()
