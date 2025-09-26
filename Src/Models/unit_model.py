from Src.Core.abstract_model import abstact_model
from Src.Core.validator import validator
from Src.Core.errors import argument_exception, operation_exception

class unit_model(abstact_model):
    __name: str = ""
    __factor: float = 1.0
    __base_unit: 'unit_model' = None
    def __init__(self, name: str, factor: float, base_unit: 'unit_model' = None):
        super().__init__()
        self.name = name
        self.factor = factor
        self.base_unit = base_unit
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, value: str):
        validator.validate(value, str)
        if len(value.strip()) == 0:
            raise argument_exception("наименование не должно быть пустым")
        self.__name = value.strip()
    @property
    def factor(self) -> float:
        return self.__factor
    @factor.setter
    def factor(self, value: float):
        validator.validate(value, (int, float))
        if value <= 0:
            raise operation_exception("коэффициент должен быть положительным")
        self.__factor = value
    @property
    def base_unit(self) -> 'unit_model':
        return self.__base_unit
    @base_unit.setter
    def base_unit(self, value: 'unit_model'):
        if value is not None and not isinstance(value, unit_model):
            raise argument_exception("базовая единица должна быть экземпляром unit_model")
        self.__base_unit = value
