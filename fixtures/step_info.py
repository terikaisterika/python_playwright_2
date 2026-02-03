import pytest
import allure


@pytest.fixture(scope="function")
def step_info(name: str, type: str = "компонентом"):
    start_step_description = f"Инфо.шаг: Начало работы с {type} {name}"
    with allure.step(start_step_description):
        pass
    yield
    end_step_description = f"Инфо.шаг: Окончание работы с {type} {name}"
    with allure.step(end_step_description):
        pass
