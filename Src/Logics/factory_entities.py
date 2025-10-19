from Src.Logics.response_csv import response_scv
from Src.Logics.response_markdown import response_markdown
from Src.Logics.response_json import response_json
from Src.Logics.response_xml import response_xml
from Src.settings_manager import settings_manager
from Src.Core.abstract_response import abstract_response
from Src.Core.validator import operation_exception

class factory_entities:
    """
    Фабрика для создания объектов форматов ответа (CSV, Markdown, JSON, XML)
    """
    __match = {
        "csv": response_scv,
        "markdown": response_markdown,
        "json": response_json,
        "xml": response_xml
    }

    def __init__(self):
        self.settings = settings_manager()

    #создаёт объект нужного формата
    def create(self, format: str) -> abstract_response:
        fmt = format.lower()
        if fmt not in self.__match:
            raise operation_exception(f"Формат не верный: {format}")
        return self.__match[fmt]()  # создаём объект нужного класса

    #создаёт объект формата, беря формат из настроек
    def create_default(self) -> abstract_response:
        #берём формат из настроек
        fmt = self.settings.response_format.lower()
        if fmt not in self.__match:
            raise operation_exception(
                f"Формат из настроек не поддерживается: {self.settings.response_format}"
            )
        return self.__match[fmt]()
