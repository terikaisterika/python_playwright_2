from app_structure.elements.base_element import BaseElement


class Link(BaseElement):
    @property
    def type(self) -> str:
        return "ссылка"
