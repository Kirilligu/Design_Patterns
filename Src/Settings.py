from Src.Models.company_model import company_model

class Settings:
    def __init__(self):
        self.company = company_model()
        self.inn = ""
        self.account = ""
        self.corr_account = ""
        self.bik = ""
        self.name = ""
        self.ownership_type = ""
    def set_inn(self, value):  #инн
        if len(value.strip()) == 12:
            self.inn = value.strip()
        else:
            raise Exception("ИНН должен быть 12 символов")

    def set_account(self, value): ##счет
        if len(value.strip()) == 11:
            self.account = value.strip()
        else:
            raise Exception("Счёт должен быть 11 символов")

    def set_corr_account(self, value): ##корр счет
        if len(value.strip()) == 11:
            self.corr_account = value.strip()
        else:
            raise Exception("Корреспондентский счёт должен быть 11 символов")

    def set_bik(self, value): ##бик
        if len(value.strip()) == 9:
            self.bik = value.strip()
        else:
            raise Exception("БИК должен быть 9 символов")

    def set_name(self, value): ##наименование
        if value.strip() != "":
            self.name = value.strip()
        else:
            raise Exception("Наименование не может быть пустым")

    def set_ownership_type(self, value): ##вид
        if len(value.strip()) == 5:
            self.ownership_type = value.strip()
        else:
            raise Exception("Вид собственности должен быть 5 символов")
