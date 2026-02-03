from playwright.sync_api import Page, expect
import allure
from typing import Pattern
from app_structure.pages.base_page import BasePage
from app_structure.components.header import Header
from app_structure.components.list_product import ListProduct


class ResultSearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.name = "страница результата поиска"
        self.header = Header(page)
        self.list_product = ListProduct(page)
