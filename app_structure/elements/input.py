import allure
from playwright.sync_api import expect

from app_structure.elements.base_element import BaseElement


class Input(BaseElement):
    @property
    def type(self):
        return "input"

    def fill(self, value: str, nth: int = 0):
        step_description = f"В {self.type} {self.name} введен текст '{value}'"

        with allure.step(step_description):
            element = self.get_element(nth)
            element.fill(value)
