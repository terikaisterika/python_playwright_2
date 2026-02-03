import allure
from playwright.sync_api import Page, expect


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page
        self.name = "базовый компонент"

    def step_info(self, start_step: bool = True):
        step_type = "Начало" if start_step else "Окончание"
        step_description = f"Инфо.шаг:{step_type} работы с компонентом {self.name}"
        with allure.step(step_description):
            pass
