from playwright.sync_api import Page, expect
import allure
from typing import Pattern


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.name = "базовая страница"

    def visit(self, url: str):
        step_description = f"Переход на страницу {self.name}. url: {url}"
        with allure.step(step_description):
            self.page.goto(url)

    def check_current_url(self, part_url: Pattern[str] | str):
        step_description = f"Текущий url соответствует паттерну {part_url.pattern}"
        with allure.step(step_description):
            expect(self.page).to_have_url(part_url)
