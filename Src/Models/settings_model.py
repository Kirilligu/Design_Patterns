from Src.Models.company_model import company_model
from Src.Core.validator import validator


######################################
# Модель настроек приложения
class settings_model:
    __company: company_model = None
    __response_format: str = "CSV"

    # Текущая организация
    @property
    def company(self) -> company_model:
        return self.__company

    @company.setter
    def company(self, value: company_model):
        validator.validate(value, company_model)
        self.__company = value

    #формат ответа (CSV, Markdown, Json, XML)
    @property
    def response_format(self) -> str:
        return self.__response_format

    @response_format.setter
    def response_format(self, value: str):
        allowed = ["CSV", "Markdown", "Json", "XML"]
        if not isinstance(value, str):
            raise ValueError("Формат ответа должен быть строкой")
        if value not in allowed:
            raise ValueError(f"Недопустимый формат ответа: {value}. Надо: {allowed}")
        self.__response_format = value