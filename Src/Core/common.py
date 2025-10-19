from Src.Core.entity_model import entity_model
from Src.Core.abstract_model import abstact_model
from Src.Core.validator import argument_exception

# Набор статических общих методов
class common:

    """
    Получить список наименований всех моделей
    """
    @staticmethod
    def get_models() -> list:
        result = []
        for  inheritor in entity_model.__subclasses__():
            result.append(inheritor.__name__)

        return result


    """
    Получить полный список полей любой модели
        - is_common = True - исключить из списка словари и списки
    """

    @staticmethod
    def get_fields(source, is_common: bool = False) -> list:
        if source is None:
            raise argument_exception("Некорректно переданы аргументы!")
        # Если это dataclass - берём поля напрямую
        if hasattr(source, "__dataclass_fields__"):
            return list(source.__dataclass_fields__.keys())
        # Иначе используем старую логику
        items = list(filter(lambda x: not x.startswith("_"), dir(source)))
        result = []

        for item in items:
            #если это свойство (property)
            attr = getattr(source.__class__, item, None)
            if isinstance(attr, property):
                value = getattr(source, item)
                #только простые типы
                if is_common and (isinstance(value, dict) or isinstance(value, list)):
                    continue

                result.append(item)

        return result

