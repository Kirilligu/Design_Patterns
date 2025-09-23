
###############################################
# Модель организации
class company_model:
    __name: str = ""
    __inn: int = 0
    __account: int = 0
    __corr_account: int = 0
    __bik: int = 0
    __ownership: str = ""

    # Наименование
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() != "":
            self.__name = value.strip()
        else:
            raise Exception("Наименование не может быть пустым")

    #инн
    @property
    def inn(self) -> int:
        return self.__inn
    @inn.setter
    def inn(self, value):
        value_str = str(value).strip()
        if value_str.isdigit() and len(value_str) == 12:
            self.__inn = int(value_str)
        else:
            raise Exception("ИНН должен быть числом из 12 цифр")

    #счёт
    @property
    def account(self) -> int:
        return self.__account
    @account.setter
    def account(self, value):
        value_str = str(value).strip()
        if value_str.isdigit() and len(value_str) == 11:
            self.__account = int(value_str)
        else:
            raise Exception("Счёт должен быть числом из 11 цифр")

    #кор счёт
    @property
    def corr_account(self) -> int:
        return self.__corr_account
    @corr_account.setter
    def corr_account(self, value):
        value_str = str(value).strip()
        if value_str.isdigit() and len(value_str) == 11:
            self.__corr_account = int(value_str)
        else:
            raise Exception("Корреспондентский счёт должен быть числом из 11 цифр")

    #бик
    @property
    def bik(self) -> int:
        return self.__bik
    @bik.setter
    def bik(self, value):
        value_str = str(value).strip()
        if value_str.isdigit() and len(value_str) == 9:
            self.__bik = int(value_str)
        else:
            raise Exception("БИК должен быть числом из 9 цифр")

    #вид собственности
    @property
    def ownership(self) -> str:
        return self.__ownership
    @ownership.setter
    def ownership(self, value: str):
        if len(value.strip()) == 5:
            self.__ownership = value.strip()
        else:
            raise Exception("Вид собственности должен быть 5 символов")
