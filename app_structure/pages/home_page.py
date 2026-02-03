from playwright.sync_api import Page, expect
import allure

from app_structure.pages.base_page import BasePage
from app_structure.components.header import Header
from app_structure.components.list_product import ListProduct


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.name = "главная страница"
        self.header = Header(page)
        self.list_product = ListProduct(page)
