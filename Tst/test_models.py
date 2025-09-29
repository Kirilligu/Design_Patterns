from Src.settings_manager import settings_manager
from Src.Models.company_model import company_model
from Src.Models.unit_model import unit_model
from Src.Models.storage_model import storage_model
from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Settings import Settings
import unittest
import os

class TestModels(unittest.TestCase):
    """
    Набор тестов (юнит + интеграция) для моделей и настроек
    """
    # ================ Юнит / мелкие проверки ================

    def test_NameEmptyAfterCreation_CompanyModel_ИмяПустое(self):
        """
        Подготовка: создать company_model без параметров
        Действие: -
        Проверка: name == ''
        """
        # Arrange
        model = company_model()
        # Act - нет действия
        # Assert
        self.assertEqual(model.name, "")

    def test_SetName_CompanyModel_УстановкаИмениНеПустого(self):
        """
        Подготовка: пустой company_model
        Действие: установить name = "test"
        Проверка: name != ""
        """
        # Arrange
        model = company_model()
        # Act
        model.name = "test"
        # Assert
        self.assertNotEqual(model.name, "")

    def test_UnitModel_CreationAndValidation(self):
        """
        Подготовка: задать name,factor,base_unit
        Действие: создать грамм и кг
        Проверки: корректные значения, исключение на отрицательный коэффициент
        """
        # Arrange
        gram = unit_model("грамм", 1)
        # Act & Assert: базовая единица
        self.assertEqual(gram.name, "грамм")
        self.assertEqual(gram.factor, 1)
        self.assertIsNone(gram.base_unit)
        # Arrange
        kg = unit_model("кг", 1000, gram)
        # Act & Assert
        self.assertEqual(kg.name, "кг")
        self.assertEqual(kg.factor, 1000)
        self.assertEqual(kg.base_unit, gram)
        with self.assertRaises(Exception):
            unit_model("ошибочная", -10)

    def test_StorageModel_NameLengthLimit(self):
        """
        Подготовка: создать storage_model
        Действие: установить корректное имя, затем слишком длинное
        Проверки: нормальное имя проходит, длинное - исключение
        """
        # Arrange
        storage = storage_model()
        # Act
        storage.name = "Склад №1"
        # Assert
        self.assertEqual(storage.name, "Склад №1")
        # Act & Assert
        with self.assertRaises(Exception):
            storage.name = "x" * 60

    # ================ Интеграционные проверки с settings_manager ================

    def test_LoadSettings_ReturnsTrue(self):
        """
        Подготовка: задать путь к settings.json
        Действие: вызвать mgr.load()
        Проверка: результат == True
        """
        # Arrange
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        mgr = settings_manager()
        mgr.file_name = os.path.abspath(file_name)
        # Act
        result = mgr.load()
        # Assert
        self.assertTrue(result)

    def test_Singleton_SettingsManager_ОдинаковыйCompany(self):
        """
        Подготовка: два экземпляра settings_manager, установить file_name
        Действие: вызвать load() у первого
        Проверка: mgr1.company == mgr2.company
        """
        # Arrange
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        mgr1 = settings_manager()
        mgr1.file_name = os.path.abspath(file_name)
        mgr2 = settings_manager()
        # Act
        mgr1.load()
        # Assert
        self.assertEqual(mgr1.company, mgr2.company)

    def test_ConvertMethod_SettingsManager(self):
        """
        Подготовка: settings_manager, словарь data
        Действие: convert(data)
        Проверка: возвращается Settings, имя компании установлено
        """
        # Arrange
        mgr = settings_manager()
        data = {"company": {"name": "TestCompany"}}
        # Act
        settings_obj = mgr.convert(data)
        # Assert
        self.assertIsInstance(settings_obj, Settings)
        self.assertEqual(settings_obj.company.name, "TestCompany")

    def test_LoadFullSettingsAndCompany(self):
        """
        Подготовка: путь к settings.json
        Действие: load + convert
        Проверки: корректный company_model, имя из JSON
        """
        # Arrange
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        mgr = settings_manager()
        mgr.file_name = os.path.abspath(file_name)
        # Act
        result = mgr.load()
        settings_obj = mgr.convert({"company": {"name": mgr.company.name}})
        # Assert
        self.assertTrue(result)
        self.assertIsInstance(settings_obj, Settings)
        self.assertIsInstance(settings_obj.company, company_model)
        self.assertEqual(settings_obj.company.name, "Рога и копыта")

    def test_LoadFromRootFolder_Settings(self):
        """
        Подготовка: путь к settings.json из корня
        Действие: load()
        Проверка: имя компании корректно загружено
        """
        # Arrange
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        mgr = settings_manager()
        mgr.file_name = os.path.abspath(file_name)
        # Act
        result = mgr.load()
        # Assert
        self.assertTrue(result)
        self.assertEqual(mgr.company.name, "Рога и копыта")

    def test_LoadFromOtherFolderAndName_Settings(self):
        """
        Подготовка: путь к другому каталогу example.json
        Действие: load()
        Проверка: имя компании соответствует заданному
        """
        # Arrange
        file_name = os.path.join(os.path.dirname(__file__), "example", "example.json")
        mgr = settings_manager()
        mgr.file_name = os.path.abspath(file_name)
        # Act
        result = mgr.load()
        # Assert
        self.assertTrue(result)
        self.assertEqual(mgr.company.name, "ООО ИГУ")

    def test_SettingsConstraints_Methods(self):
        """
        Подготовка: instantiate Settings
        Действие: вызов методов set_inn, set_account и др с корректными и некорректными значениями
        Проверка: корректные установки проходят, некорректные - исключения (вывод в print)
        """
        # Arrange
        s = Settings()
        # Act & Assert
        # инн
        try:
            s.set_inn("123456789012")  # корректное
            s.set_inn("123")           # некорректное
        except Exception as e:
            print("ИНН:", e)
        # счёт
        try:
            s.set_account("12345678901")
            s.set_account("123")
        except Exception as e:
            print("Счёт:", e)
        # корр.счёт
        try:
            s.set_corr_account("12345678901")
            s.set_corr_account("123")
        except Exception as e:
            print("Корр. счёт:", e)
        # бик
        try:
            s.set_bik("123456789")
            s.set_bik("123")
        except Exception as e:
            print("БИК:", e)
        # наименование
        try:
            s.set_name("Рога и копыта")
            s.set_name("")
        except Exception as e:
            print("Наименование:", e)
        # вид собственности
        try:
            s.set_ownership_type("OOO01")
            s.set_ownership_type("1234")
        except Exception as e:
            print("Вид собственности:", e)

    def test_CreateCompanyFromSettings_CompanyModel(self):
        """
        Подготовка: загрузка настроек, установка валидных данных вручную
        Действие: создание company_model из mgr.company
        Проверки: все поля company совпадают
        """
        # Arrange
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        mgr = settings_manager()
        mgr.file_name = os.path.abspath(file_name)
        mgr.load()
        # вручную установка валидных значений
        mgr.company.name = "Рога и копыта"
        mgr.company.inn = "123456789012"
        mgr.company.account = "12345678901"
        mgr.company.corr_account = "12345678901"
        mgr.company.bik = "123456789"
        mgr.company.ownership = "OOO01"
        # Act
        company = company_model(mgr.company)
        # Assert
        self.assertEqual(company.name, mgr.company.name)
        self.assertEqual(company.inn, mgr.company.inn)
        self.assertEqual(company.account, mgr.company.account)
        self.assertEqual(company.corr_account, mgr.company.corr_account)
        self.assertEqual(company.bik, mgr.company.bik)
        self.assertEqual(company.ownership, mgr.company.ownership)

if __name__ == '__main__':
    unittest.main()
