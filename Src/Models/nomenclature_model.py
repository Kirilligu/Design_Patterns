from Src.Core.abstract_model import abstact_model
from Src.Models.unit_model import unit_model
from Src.Models.group_model import group_model
from Src.Core.validator import validator
from Src.Core.errors import argument_exception

class nomenclature_model(abstact_model):
    __name: str = ""
    __full_name: str = ""
    __unit: unit_model = None
    __group: group_model = None
    def __init__(self, name: str, full_name: str, unit: unit_model, group: group_model):
        super().__init__()
        self.name = name
        self.full_name = full_name
        self.unit = unit
        self.group = group

    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, value: str):
        validator.validate(value, str)
        if len(value.strip()) > 50:
            raise argument_exception("обычное наименование не может быть длиннее 50 символов")
        self.__name = value.strip()

    @property
    def full_name(self) -> str:
        return self.__full_name
    @full_name.setter
    def full_name(self, value: str):
        validator.validate(value, str)
        if len(value.strip()) > 255:
            raise argument_exception("полное наименование не может быть длиннее 255 символов")
        self.__full_name = value.strip()

    @property
    def unit(self) -> unit_model:
        return self.__unit
    @unit.setter
    def unit(self, value: unit_model):
        if not isinstance(value, unit_model):
            raise argument_exception("поле unit должно ссылаться на unit_model")
        self.__unit = value

    @property
    def group(self) -> group_model:
        return self.__group
    @group.setter
    def group(self, value: group_model):
        if not isinstance(value, group_model):
            raise argument_exception("поле group должно ссылаться на group_model")
        self.__group = value
