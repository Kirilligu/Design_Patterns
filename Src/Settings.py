from Src.Models.company_model import company_model

class Settings:
    def __init__(self):
        self.company = company_model()
    def set_inn(self, value):
        self.company.inn = value
    def set_account(self, value):
        self.company.account = value
    def set_corr_account(self, value):
        self.company.corr_account = value
    def set_bik(self, value):
        self.company.bik = value
    def set_name(self, value):
        self.company.name = value
    def set_ownership_type(self, value):
        self.company.ownership = value
