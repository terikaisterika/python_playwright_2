import allure
from playwright.sync_api import Page, expect
from app_structure.elements.link import Link
from app_structure.components.base_component import BaseComponent
from typing import Literal, Pattern


class ListProduct(BaseComponent):
    def __init__(self, page):

        super().__init__(page)
        self.name = "компонент 'Список товаров'"
        self.product_name_list_links = Link(
            self.page,
            "div.thumbnails.list-inline a.prdocutname",
            "список наименований товаров",
        )

    def check_count_products_after_search(self, expected_count: int):
        list_products = self.product_name_list_links.get_element(-1)
        count_products = list_products.count()
        step_description = f"Количество товаров на странице = {count_products}. Должно быть {expected_count}"
        with allure.step(step_description):
            expect(list_products, step_description).to_have_count(expected_count)

    def check_count_products_after_search_relative(
        self, sign_comparison: Literal["more", "less"] = "more", expected_count: int = 0
    ):
        list_products = self.product_name_list_links.get_element(-1)
        count_products = list_products.count()
        correction = "больше" if sign_comparison == "more" else "меньше"
        step_description = f"Количество товаров на странице = {count_products} должно быть {correction} {expected_count}"
        with allure.step(step_description):
            if sign_comparison == "more":
                assert count_products > expected_count, step_description
            elif sign_comparison == "less":
                assert count_products < expected_count, step_description

    def check_search_word_in_product_name(self, phrase: str | Pattern[str]):
        step_description = f"Проверка наличия '{phrase}' в наименовании товара"
        list_products = self.product_name_list_links.get_element(-1)
        with allure.step(step_description):
            for link in list_products.all():
                msg = f"В наименовании товара '{link.text_content()}' должно быть искомое '{phrase}'"
                print(msg)
                expect(link, msg).to_have_text(phrase)
