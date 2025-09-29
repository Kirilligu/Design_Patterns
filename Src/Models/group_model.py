from Src.Core.abstract_model import abstact_model
from Src.Core.validator import validator
from Src.Core.errors import argument_exception

class group_model(abstact_model):
    __name: str = ""
    def __init__(self, name: str = ""):
        super().__init__()
        self.name = name
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, value: str):
        validator.validate(value, str)
        if len(value.strip()) > 50:
            raise argument_exception("наименование группы не может быть длиннее 50 символов")
        self.__name = value.strip()
