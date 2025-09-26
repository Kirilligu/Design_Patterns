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

    # Провери создание основной модели
    # Данные после создания должны быть пустыми
    def test_empty_createmodel_companymodel(self):
        model = company_model()
        assert model.name == ""

    # Проверить создание основной модели
    # Данные меняем. Данные должны быть
    def test_notEmpty_createmodel_companymodel(self):
        model = company_model()
        model.name = "test"
        assert model.name != ""

    # Проверить создание основной модели
    # Данные загружаем через json настройки
    def test_load_createmodel_companymodel(self):
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        file_name = os.path.abspath(file_name)

        mgr = settings_manager()
        mgr.file_name = file_name
        result = mgr.load()
        assert result == True

    # Проверить создание основной модели
    # Данные загружаем. Проверяем работу Singletone
    def test_loadCombo_createmodel_companymodel(self):
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        file_name = os.path.abspath(file_name)

        mgr1 = settings_manager()
        mgr1.file_name = file_name
        mgr2 = settings_manager()
        mgr1.load()

        assert mgr1.company == mgr2.company

    # Проверка convert
    def test_convert_createmodel_settings(self):
        mgr = settings_manager()
        data = {"company": {"name": "TestCompany"}}
        settings_obj = mgr.convert(data)
        self.assertIsInstance(settings_obj, Settings)
        self.assertEqual(settings_obj.company.name, "TestCompany")

    # проверка загрузки Settings из JSON
    def test_load_full_settings(self):
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

    # проверка загрузки из корневого каталога
    def test_load_from_root_folder(self):
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        file_name = os.path.abspath(file_name)
        mgr = settings_manager()
        mgr.file_name = file_name
        result = mgr.load()
        self.assertTrue(result)
        self.assertEqual(mgr.company.name, "Рога и копыта")

    # проверка загрузки из другого каталога и с другим именем файла
    def test_load_from_other_folder_and_name(self):
        file_name = os.path.join(os.path.dirname(__file__), "example", "example.json")
        file_name = os.path.abspath(file_name)
        mgr = settings_manager()
        mgr.file_name = file_name
        result = mgr.load()
        self.assertTrue(result)
        self.assertEqual(mgr.company.name, "ООО ИГУ")

    # проверка ограничений Settings
    def test_settings_constraints(self):
        s = Settings()
        # инн
        try:
            s.set_inn("123456789012")
            s.set_inn("123")
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

    # проверка storage_model
    def test_storage_model(self):
        storage = storage_model()
        storage.name = "Склад №1"
        self.assertEqual(storage.name, "Склад №1")
        #ограничения длины
        with self.assertRaises(Exception):
            storage.name = "x" * 60  #больше 50 символов
    def test_create_company_from_settings(self):
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
        company = company_model(mgr.company)
        self.assertEqual(company.name, mgr.company.name)
        self.assertEqual(company.inn, mgr.company.inn)
        self.assertEqual(company.account, mgr.company.account)
        self.assertEqual(company.corr_account, mgr.company.corr_account)
        self.assertEqual(company.bik, mgr.company.bik)
        self.assertEqual(company.ownership, mgr.company.ownership)

    def test_unit_model(self):
        #грамм
        gram = unit_model("грамм", 1)
        self.assertEqual(gram.name, "грамм")
        self.assertEqual(gram.factor, 1)
        self.assertIsNone(gram.base_unit)

        #килограмм с коэфф
        kg = unit_model("кг", 1000, gram)
        self.assertEqual(kg.name, "кг")
        self.assertEqual(kg.factor, 1000)
        self.assertEqual(kg.base_unit, gram)
        with self.assertRaises(Exception):
            unit_model("ошибочная", -10)

if __name__ == '__main__':
    unittest.main()
