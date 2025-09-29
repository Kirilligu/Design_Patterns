from Src.Core.abstract_model import abstact_model
from Src.Core.validator import validator
from Src.Core.errors import argument_exception
from Src.Settings import Settings


class organization_model(abstact_model):
    __inn: str = ""
    __bik: str = ""
    __account: str = ""
    __ownership: str = ""

    def __init__(self, settings: Settings = None):
        super().__init__(settings.company.name if settings else "")
        if settings:
            self.inn = settings.company.inn
            self.account = settings.company.account
            self.bik = settings.company.bik
            self.ownership = settings.company.ownership

    @property
    def inn(self) -> str:
        return self.__inn
    @inn.setter
    def inn(self, value: str):
        validator.validate(value, str)
        value = value.strip()
        if not value.isdigit() or len(value) != 12:
            raise argument_exception("ИНН должен содержать 12 цифр")
        self.__inn = value

    @property
    def account(self) -> str:
        return self.__account
    @account.setter
    def account(self, value: str):
        validator.validate(value, str)
        value = value.strip()
        if not value.isdigit() or len(value) < 11:
            raise argument_exception("счет должен содержать минимум 11 цифр")
        self.__account = value

    @property
    def bik(self) -> str:
        return self.__bik
    @bik.setter
    def bik(self, value: str):
        validator.validate(value, str)
        value = value.strip()
        if not value.isdigit() or len(value) != 9:
            raise argument_exception("БИК должен содержать 9 цифр")
        self.__bik = value

    @property
    def ownership(self) -> str:
        return self.__ownership
    @ownership.setter
    def ownership(self, value: str):
        validator.validate(value, str)
        value = value.strip()
        if len(value) != 5:
            raise argument_exception("вид собственности должен содержать 5 символов")
        self.__ownership = value
