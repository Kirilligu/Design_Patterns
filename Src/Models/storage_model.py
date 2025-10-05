from Src.Core.abstract_model import abstact_model
from Src.Core.errors import argument_exception

class storage_model(abstact_model):
    def __init__(self, name: str = ""):
        super().__init__()
        self.name = name
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str):
        if len(value.strip()) > 50:
            raise argument_exception("наименование склада не может быть длиннее 50 символов")
        self._name = value.strip()
