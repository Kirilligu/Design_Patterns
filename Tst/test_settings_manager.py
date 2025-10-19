import unittest
from Src.settings_manager import settings_manager
from Src.Settings import Settings
from Src.Models.company_model import company_model
import os, json

class TestSettingsManager(unittest.TestCase):
    """
    Проверка работы класса settings_manager
    """
    def setUp(self):
        """
        Подготовка: создаём временный settings.json для тестов
        """
        self.test_file = "test_settings.json"
        data = {
            "company": {"name": "какая-то компания"},
            "response_format": "CSV"
        }
        with open(self.test_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def tearDown(self):
        """
        удаляем временный файл после тестов
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_valid_settings(self):
        """
        Подготовка: создаём менеджер и указываем корректный файл настроек
        Действие: выполняем загрузку через load()
        Проверка: данные компании и формат ответа загружены верно
        """
        mgr = settings_manager()
        mgr.file_name = self.test_file
        result = mgr.load()

        # Assert
        self.assertTrue(result, "Настройки не загрузились")
        self.assertEqual(mgr.company.name, "Какая-то компания")
        self.assertEqual(mgr._settings_manager__sett.response_format, "CSV")

    def test_default_settings(self):
        """
        Подготовка: создаём менеджер без указания файла
        Действие: вызываем set_default()
        Проверка: создаются стандартные значения
        """
        mgr = settings_manager()
        mgr.set_default()

        # Assert
        self.assertIsInstance(mgr.company, company_model)
        self.assertIsInstance(mgr._settings_manager__sett, Settings)
        self.assertEqual(mgr.company.name, "Рога и копыта")

    def test_file_not_found(self):
        """
        Подготовка: создаём менеджер и указываем несуществующий файл
        Действие: пытаемся установить file_name
        Проверка: выбрасывается исключение
        """
        mgr = settings_manager()
        # Assert
        with self.assertRaises(Exception):
            mgr.file_name = "nonexistent.json"
