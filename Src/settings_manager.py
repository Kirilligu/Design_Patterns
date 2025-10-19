from Src.Models.company_model import company_model
from Src.Settings import Settings
import os
import json

#######################################################
# Менеджер настроек
# Управляет настройками и хранит параметры приложения
class settings_manager:
    __fname: str = ""
    __company: company_model = None
    __sett: Settings = None

    # Singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.set_default()

    @property
    def settings(self):
        """Возвращает объект настроек (Settings)"""
        return self.__sett

    # Параметры организации из настроек
    @property
    def company(self) -> company_model:
        return self.__company

    @property
    def file_name(self) -> str:
        return self.__fname
    def _find_settings_file(self, path):
        if os.path.isabs(path) and os.path.exists(path):
            return path
        try_path1 = os.path.join(os.getcwd(), path)
        if os.path.exists(try_path1):
            return try_path1
        try_path2 = os.path.join(os.path.dirname(__file__), path)
        if os.path.exists(try_path2):
            return try_path2
        return ""

    # Полный путь к файлу настроек
    @file_name.setter
    def file_name(self, value: str):
        if value.strip() == "":
            return
        found = self._find_settings_file(value.strip())
        if found:
            self.__fname = found
        else:
            raise Exception(f"Не найден файл настроек: {value}")
    def convert(self, data: dict):
        if not hasattr(self, "_sett") or self.__sett is None:
            self.__sett = Settings()
            self.__sett.company = self.__company
        if "company" in data:
            item = data["company"]
            if "name" in item:
                self.__company.name = item["name"]
            if "inn" in item:
                self.__company.inn = item["inn"]
            if "account" in item:
                self.__company.account = item["account"]
            if "corr_account" in item:
                self.__company.corr_account = item["corr_account"]
            if "bik" in item:
                self.__company.bik = item["bik"]
            if "ownership" in item:
                self.__company.ownership = item["ownership"]

        #загружаем формат ответа, если есть
        if "response_format" in data:
            fmt = data["response_format"]
            self.__sett.response_format = fmt

        return self.__sett

    # Загрузить настройки из Json файла
    def load(self):
        if self.__fname.strip() == "":
            raise Exception("Не найден файл настроек!")

        try:
            with open(self.__fname.strip(), 'r', encoding="utf-8") as f:
                data = json.load(f)
                self.__sett = self.convert(data)
                return True
        except:
            return False

    @property
    def response_format(self) -> str:
        # Возвращаем формат из self.__sett, если есть, иначе CSV
        return getattr(self.__sett, "response_format", "CSV")

    @response_format.setter
    def response_format(self, value: str):
        valid_formats = ["CSV", "MARKDOWN", "JSON", "XML"]
        if value.upper() not in valid_formats:
            raise ValueError(f"Неверный формат ответа: {value}")
        self.__sett.response_format = value.upper()
    # Параметры настроек по умолчанию
    def set_default(self):
        self.__company = company_model()
        self.__company.name = "Рога и копыта"
        self.__sett = Settings()
        self.__sett.company = self.__company
        self.__sett.response_format = "CSV"  #формат по умолчанию