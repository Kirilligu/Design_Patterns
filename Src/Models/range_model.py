from Src.Core.entity_model import entity_model
from Src.Core.validator import validator, argument_exception

"""
Модель единицы измерения
"""

class range_model(entity_model):
    __value: int = 1
    __base: 'range_model' = None

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        validator.validate(value, int)
        if value <= 0:
            raise argument_exception("Некорректный аргумент!")
        self.__value = value

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        self.__base = value

    @staticmethod
    def create_gramm():
        return range_model.create("грамм", None)

    @staticmethod
    def create_kill():
        gramm = range_model.create_gramm()
        return range_model.create("килограмм", gramm)

    @staticmethod
    def create(name: str, base=None):
        validator.validate(name, str)
        if base is not None:
            validator.validate(base, range_model)
        item = range_model()
        item.name = name
        item.base = base
        return item
