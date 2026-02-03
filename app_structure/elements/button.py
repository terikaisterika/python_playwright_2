from app_structure.elements.base_element import BaseElement


class Button(BaseElement):
    @property
    def type(self) -> str:
        return "кнопка"
