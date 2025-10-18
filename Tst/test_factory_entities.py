import unittest
from Src.Logics.factory_entities import factory_entities
from Src.settings_manager import settings_manager
from Src.Logics.response_csv import response_scv
from Src.Logics.response_markdown import response_markdown
from Src.Logics.response_json import response_json
from Src.Logics.response_xml import response_xml
from Src.Core.validator import operation_exception

class TestFactoryEntities(unittest.TestCase):
    def setUp(self):
        # Создаём фабрику и настройки
        self.factory = factory_entities()
        self.settings = self.factory.settings
        #формат по умолчанию для тестов
        self.settings.settings.response_format = "CSV"

    def test_create_csv(self):
        """Проверка метода create с форматом CSV"""
        try:
            response = self.factory.create("csv")
            self.assertIsInstance(response, response_scv)
        except Exception as e:
            self.fail(f"Ошибка при create('csv'): {e}")

    def test_create_markdown(self):
        """Проверка метода create с форматом Markdown"""
        try:
            response = self.factory.create("markdown")
            self.assertIsInstance(response, response_markdown)
        except Exception as e:
            self.fail(f"Ошибка при create('markdown'): {e}")

    def test_create_json(self):
        """Проверка метода create с форматом JSON"""
        try:
            response = self.factory.create("json")
            self.assertIsInstance(response, response_json)
        except Exception as e:
            self.fail(f"Ошибка при create('json'): {e}")

    def test_create_xml(self):
        """Проверка метода create с форматом XML"""
        try:
            response = self.factory.create("xml")
            self.assertIsInstance(response, response_xml)
        except Exception as e:
            self.fail(f"Ошибка при create('xml'): {e}")

    def test_create_default_csv(self):
        """Проверка метода create_default, берёт формат из настроек"""
        try:
            response = self.factory.create_default()
            self.assertIsInstance(response, response_scv)
        except Exception as e:
            self.fail(f"Ошибка при create_default(): {e}")

    def test_create_invalid_format(self):
        """Проверка, что create выбрасывает ошибку на некорректный формат"""
        with self.assertRaises(operation_exception):
            self.factory.create("invalid")

    def test_create_default_invalid_format(self):
        """Проверка, что create_default выбрасывает ошибку при неправильном формате в настройках"""
        self.settings.settings.response_format = "INVALID"
        with self.assertRaises(operation_exception):
            self.factory.create_default()

if __name__ == "__main__":
    unittest.main()
