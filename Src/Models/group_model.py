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
        self.factory = factory_entities()
        self.settings = self.factory.settings
    def test_create_csv(self):
        """Проверка метода create с форматом CSV"""
        response = self.factory.create("csv")
        self.assertIsInstance(response, response_scv)
    def test_create_markdown(self):
        """Проверка метода create с форматом Markdown"""
        response = self.factory.create("markdown")
        self.assertIsInstance(response, response_markdown)
    def test_create_json(self):
        """Проверка метода create с форматом JSON"""
        response = self.factory.create("json")
        self.assertIsInstance(response, response_json)
    def test_create_xml(self):
        """Проверка метода create с форматом XML"""
        response = self.factory.create("xml")
        self.assertIsInstance(response, response_xml)
    def test_create_default_csv(self):
        """Проверка create_default берёт формат из настроек"""
        self.settings.settings.response_format = "CSV"
        response = self.factory.create_default()
        self.assertIsInstance(response, response_scv)
    def test_create_default_markdown(self):
        self.settings.settings.response_format = "Markdown"
        response = self.factory.create_default()
        self.assertIsInstance(response, response_markdown)
    def test_create_default_json(self):
        self.settings.settings.response_format = "Json"
        response = self.factory.create_default()
        self.assertIsInstance(response, response_json)
    def test_create_default_xml(self):
        self.settings.settings.response_format = "XML"
        response = self.factory.create_default()
        self.assertIsInstance(response, response_xml)
    def test_create_invalid_format(self):
        """Проверка create выбрасывает ошибку на некорректный формат"""
        with self.assertRaises(operation_exception):
            self.factory.create("invalid")
    def test_create_default_invalid_format(self):
        """Проверка create_default выбрасывает ошибку при неправильном формате"""
        self.settings.settings.response_format = "INVALID"
        with self.assertRaises(operation_exception):
            self.factory.create_default()
