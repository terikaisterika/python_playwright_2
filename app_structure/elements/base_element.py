import allure
from typing import Pattern, Union
from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str) -> Locator:
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type(self):
        return "базовый элемент"

    def get_element(self, nth: int = 0) -> Locator:
        step_description = (
            f"Получение элемента с локатором {self.locator} по индексу {nth}"
        )
        with allure.step(step_description):
            # element - один элемент, если nth больше или равно 0
            # список элементов, если nth меньше 0
            element = (
                self.page.locator(self.locator).nth(nth)
                if nth >= 0
                else self.page.locator(self.locator)
            )
            return element

    def click(self, nth: int = 0, force: bool = False):
        step_description = f"Нажатие на {self.type} {self.name}"
        with allure.step(step_description):
            element = self.get_element(nth)
            element.click(force=force)
