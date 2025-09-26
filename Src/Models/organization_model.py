from Src.Core.abstract_model import abstact_model
from Src.Settings import Settings

class organization_model(abstact_model):
    __inn: int = 0
    __bik: int = 0
    __account: int = 0
    __ownership: str = ""
    def __init__(self, settings: Settings = None):
        super().__init__(settings.company.name if settings else "")
        if settings:
            self.inn = settings.company.inn
            self.account = settings.company.account
            self.bik = settings.company.bik
            self.ownership = settings.company.ownership
    @property
    def inn(self):
        return self.__inn
    @inn.setter
    def inn(self, value):
        value_str = str(value).strip()
        if value_str.isdigit() and len(value_str) == 12:
            self.__inn = int(value_str)
        else:
            raise Exception("ИНН должен быть числом из 12 цифр")

    @property
    def account(self):
        return self.__account
    @account.setter
    def account(self, value):
        value_str = str(value).strip()
        if value_str.isdigit() and len(value_str) == 11:
            self.__account = int(value_str)
        else:
            raise Exception("счёт должен быть числом из 11 цифр")
    @property
    def bik(self):
        return self.__bik
    @bik.setter
    def bik(self, value):
        value_str = str(value).strip()
        if value_str.isdigit() and len(value_str) == 9:
            self.__bik = int(value_str)
        else:
            raise Exception("БИК должен быть числом из 9 цифр")

    @property
    def ownership(self):
        return self.__ownership
    @ownership.setter
    def ownership(self, value):
        if len(value.strip()) == 5:
            self.__ownership = value.strip()
        else:
            raise Exception("вид собственности должен быть 5 символов")
