from Src.settings_manager import settings_manager
from Src.Models.company_model import company_model
from Src.Models.unit_model import unit_model
from Src.Models.storage_model import storage_model
from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Settings import Settings
import unittest
import os

class test_models(unittest.TestCase):
    """
    Полный набор тестов для моделей и работы с настройками.
    Разделение:
    - Юнит-тесты: проверка отдельных классов и методов
    - Интеграционные тесты: работа с settings_manager, загрузка JSON
    - Функциональные / E2E: проверка сценариев создания и использования объектов
    """

    # ----------------- ЮНИТ-ТЕСТЫ -----------------

    def test_EmptyCompanyModel_NameEmptyAfterCreation(self):
        """Проверка создания объекта company_model без параметров.
        Должно быть пустое имя компании"""
        model = company_model()
        assert model.name == ""

    def test_SetCompanyModel_NameIsNotEmpty(self):
        """Проверка установки имени в company_model.
        После установки имя не должно быть пустым"""
        model = company_model()
        model.name = "test"
        assert model.name != ""

    def test_UnitModel_CreationAndFactorValidation(self):
        """Проверка создания единиц измерения unit_model и проверки коэффициента.
        Создание грамм, кг и проверка базовой единицы.
        Проверка исключения при отрицательном коэффициенте"""
        gram = unit_model("грамм", 1)
        self.assertEqual(gram.name, "грамм")
        self.assertEqual(gram.factor, 1)
        self.assertIsNone(gram.base_unit)
        kg = unit_model("кг", 1000, gram)
        self.assertEqual(kg.name, "кг")
        self.assertEqual(kg.factor, 1000)
        self.assertEqual(kg.base_unit, gram)
        with self.assertRaises(Exception):
            unit_model("ошибочная", -10)

    def test_StorageModel_NameLengthValidation(self):
        """Проверка создания storage_model и ограничения длины имени.
        Попытка задать слишком длинное имя вызывает исключение"""
        storage = storage_model()
        storage.name = "Склад №1"
        self.assertEqual(storage.name, "Склад №1")
        with self.assertRaises(Exception):
            storage.name = "x" * 60

    # ----------------- ИНТЕГРАЦИОННЫЕ ТЕСТЫ -----------------

    def test_LoadCompanyModel_FromJSON_ReturnsTrue(self):
        """Проверка загрузки company_model через settings_manager из JSON файла.
        Метод load должен вернуть True"""
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        file_name = os.path.abspath(file_name)
        mgr = settings_manager()
        mgr.file_name = file_name
        result = mgr.load()
        assert result == True

    def test_SettingsManager_Singleton_ReturnsSameCompany(self):
        """Проверка работы singleton settings_manager.
        Два объекта менеджера должны иметь одинаковый company"""
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        file_name = os.path.abspath(file_name)
        mgr1 = settings_manager()
        mgr1.file_name = file_name
        mgr2 = settings_manager()
        mgr1.load()
        assert mgr1.company == mgr2.company

    def test_ConvertSettings_ReturnsSettingsObject(self):
        """Проверка метода convert settings_manager.
        Должен возвращать объект Settings с корректным названием компании"""
        mgr = settings_manager()
        data = {"company": {"name": "TestCompany"}}
        settings_obj = mgr.convert(data)
        self.assertIsInstance(settings_obj, Settings)
        self.assertEqual(settings_obj.company.name, "TestCompany")

    def test_LoadFullSettingsFromJSON(self):
        """Проверка полной загрузки Settings из JSON.
        Все свойства company_model должны соответствовать ожидаемым значениям"""
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        file_name = os.path.abspath(file_name)
        mgr = settings_manager()
        mgr.file_name = file_name
        result = mgr.load()
        settings_obj = mgr.convert({"company": {"name": mgr.company.name}})
        self.assertTrue(result)
        self.assertIsInstance(settings_obj, Settings)
        self.assertIsInstance(settings_obj.company, company_model)
        self.assertEqual(settings_obj.company.name, "Рога и копыта")

    def test_LoadFromRootFolder_Settings(self):
        """Проверка загрузки настроек из корневого каталога"""
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        file_name = os.path.abspath(file_name)
        mgr = settings_manager()
        mgr.file_name = file_name
        result = mgr.load()
        self.assertTrue(result)
        self.assertEqual(mgr.company.name, "Рога и копыта")

    def test_LoadFromOtherFolderAndName(self):
        """Проверка загрузки настроек из другого каталога и с другим именем файла"""
        file_name = os.path.join(os.path.dirname(__file__), "example", "example.json")
        file_name = os.path.abspath(file_name)
        mgr = settings_manager()
        mgr.file_name = file_name
        result = mgr.load()
        self.assertTrue(result)
        self.assertEqual(mgr.company.name, "ООО ИГУ")

    def test_SettingsConstraints_Validation(self):
        """Проверка корректной работы ограничений Settings.
        Проверка INN, счета, корр.счета, БИК, имени, вида собственности"""
        s = Settings()
        #ИНН
        try:
            s.set_inn("123456789012")
            s.set_inn("123")
        except Exception as e:
            print("ИНН:", e)
        #счет
        try:
            s.set_account("12345678901")
            s.set_account("123")
        except Exception as e:
            print("Счёт:", e)
        #корр.счет
        try:
            s.set_corr_account("12345678901")
            s.set_corr_account("123")
        except Exception as e:
            print("Корр. счёт:", e)
        #БИК
        try:
            s.set_bik("123456789")
            s.set_bik("123")
        except Exception as e:
            print("БИК:", e)
        #наименование
        try:
            s.set_name("Рога и копыта")
            s.set_name("")
        except Exception as e:
            print("Наименование:", e)
        #вид собственности
        try:
            s.set_ownership_type("OOO01")
            s.set_ownership_type("1234")
        except Exception as e:
            print("Вид собственности:", e)

    def test_CreateCompanyFromSettings(self):
        """Создание объекта company_model из настроек.
        Проверка всех свойств на соответствие исходным значениям"""
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        file_name = os.path.abspath(file_name)
        mgr = settings_manager()
        mgr.file_name = file_name
        result = mgr.load()
        self.assertTrue(result)
        mgr.company.name = "Рога и копыта"
        mgr.company.inn = "123456789012"
        mgr.company.account = "12345678901"
        mgr.company.corr_account = "12345678901"
        mgr.company.bik = "123456789"
        mgr.company.ownership = "OOO01"
        company = company_model(mgr.company)
        self.assertEqual(company.name, mgr.company.name)
        self.assertEqual(company.inn, mgr.company.inn)
        self.assertEqual(company.account, mgr.company.account)
        self.assertEqual(company.corr_account, mgr.company.corr_account)
        self.assertEqual(company.bik, mgr.company.bik)
        self.assertEqual(company.ownership, mgr.company.ownership)


if __name__ == '__main__':
    unittest.main()
