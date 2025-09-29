from Src.Core.abstract_model import abstact_model
from Src.Core.validator import validator
from Src.Core.errors import argument_exception

class company_model(abstact_model):
    __name: str = ""
    __inn: str = ""
    __account: str = ""
    __corr_account: str = ""
    __bik: str = ""
    __ownership: str = ""
    def __init__(self, settings_obj=None):
        super().__init__()
        if settings_obj:
            self.name = getattr(settings_obj, "name", "")
            self.inn = getattr(settings_obj, "inn", "")
            self.account = getattr(settings_obj, "account", "")
            self.corr_account = getattr(settings_obj, "corr_account", "")
            self.bik = getattr(settings_obj, "bik", "")
            self.ownership = getattr(settings_obj, "ownership", "")

    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, value: str):
        validator.validate(value, str, len_=50)
        if not value.strip():
            raise argument_exception("наименование организации не может быть пустым")
        self.__name = value.strip()

    @property
    def inn(self) -> str:
        return self.__inn
    @inn.setter
    def inn(self, value: str):
        validator.validate(value, str, len_=12)
        if len(value.strip()) != 12:
            raise argument_exception("ИНН должен содержать ровно 12 символов")
        self.__inn = value.strip()

    @property
    def account(self) -> str:
        return self.__account
    @account.setter
    def account(self, value: str):
        validator.validate(value, str, len_=20)
        if len(value.strip()) < 11:
            raise argument_exception("счет должен содержать минимум 11 символов")
        self.__account = value.strip()

    @property
    def corr_account(self) -> str:
        return self.__corr_account
    @corr_account.setter
    def corr_account(self, value: str):
        validator.validate(value, str, len_=20)
        if len(value.strip()) < 11:
            raise argument_exception("корреспондентский счет должен содержать минимум 11 символов")
        self.__corr_account = value.strip()

    @property
    def bik(self) -> str:
        return self.__bik
    @bik.setter
    def bik(self, value: str):
        validator.validate(value, str, len_=9)
        if len(value.strip()) != 9:
            raise argument_exception("БИК должен содержать ровно 9 символов")
        self.__bik = value.strip()

    @property
    def ownership(self) -> str:
        return self.__ownership
    @ownership.setter
    def ownership(self, value: str):
        validator.validate(value, str, len_=10)
        if len(value.strip()) < 4:
            raise argument_exception("форма собственности должна содержать минимум 4 символа")
        self.__ownership = value.strip()
