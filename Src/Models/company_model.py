
###############################################
# Модель организации
class company_model:
    __name: str = ""
    __inn: str = ""
    __account: str = ""
    __corr_account: str = ""
    __bik: str = ""
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
    def inn(self) -> str:
        return self.__inn
    @inn.setter
    def inn(self, value: str):
        if len(value.strip()) == 12:
            self.__inn = value.strip()
        else:
            raise Exception("ИНН должен быть 12 символов")
    #счет
    @property
    def account(self) -> str:
        return self.__account
    @account.setter
    def account(self, value: str):
        if len(value.strip()) == 11:
            self.__account = value.strip()
        else:
            raise Exception("Счёт должен быть 11 символов")

    #корр счёт
    @property
    def corr_account(self) -> str:
        return self.__corr_account
    @corr_account.setter
    def corr_account(self, value: str):
        if len(value.strip()) == 11:
            self.__corr_account = value.strip()
        else:
            raise Exception("Корреспондентский счёт должен быть 11 символов")

    #бик
    @property
    def bik(self) -> str:
        return self.__bik
    @bik.setter
    def bik(self, value: str):
        if len(value.strip()) == 9:
            self.__bik = value.strip()
        else:
            raise Exception("БИК должен быть 9 символов")

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
