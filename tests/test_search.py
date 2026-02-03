import allure
import pytest
import re
from playwright.sync_api import Page, expect
from app_structure.pages.home_page import HomePage
from app_structure.pages.result_search_page import ResultSearchPage


# Переделать
@pytest.mark.regression
@pytest.mark.search
class TestSearch:
    @allure.title("Поиск по части слова с множественным результатом")
    def test_search_by_part_name(
        self,
        page: Page,
        settings,
    ):
        searchWord = re.compile("bronzer", re.IGNORECASE)
        home_page = HomePage(page)
        home_page.visit(f"{settings.base_url}")
        home_page.check_current_url(re.compile("automationteststore"))
        home_page.header.step_info()
        home_page.header.find_product(searchWord.pattern)
        home_page.header.step_info(False)

        result_search_page = ResultSearchPage(page)
        result_search_page.list_product.step_info()
        result_search_page.check_current_url(searchWord)
        result_search_page.list_product.check_count_products_after_search_relative()
        result_search_page.list_product.check_search_word_in_product_name(searchWord)
        result_search_page.list_product.step_info(False)
