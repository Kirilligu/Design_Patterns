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

    # Параметры настроек по умолчанию
    def set_default(self):
        self.__company = company_model()
        self.__company.name = "Рога и копыта"
        self.__sett = Settings()
        self.__sett.company = self.__company
