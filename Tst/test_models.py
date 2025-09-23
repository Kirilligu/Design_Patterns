from Src.settings_manager import settings_manager
from Src.Models.company_model import company_model
from Src.Settings import Settings
import unittest
import os

class test_models(unittest.TestCase):

    # Провери создание основной модели
    # Данные после создания должны быть пустыми
    def test_empty_createmodel_companymodel(self):
        # Подготовка
        model = company_model()

        # Действие

        # Проверки
        assert model.name == ""

    # Проверить создание основной модели
    # Данные меняем. Данные должны быть
    def test_notEmpty_createmodel_companymodel(self):
        # Подготовка
        model = company_model()

        # Действие
        model.name = "test"
        # Проверки
        assert model.name != ""

    # Проверить создание основной модели
    # Данные загружаем через json настройки
    def test_load_createmodel_companymodel(self):
        # Подготовка
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        file_name = os.path.abspath(file_name)

        mgr = settings_manager()
        mgr.file_name = file_name
        # Дейсвтие
        result = mgr.load()
        assert result == True

    # Проверить создание основной модели
    # Данные загружаем. Проверяем работу Singletone
    def test_loadCombo_createmodel_companymodel(self):
        # Подготовка
        file_name = os.path.join(os.path.dirname(__file__), "..", "settings.json")
        file_name = os.path.abspath(file_name)

        mgr1 = settings_manager()
        mgr1.file_name = file_name
        mgr2 = settings_manager()
        # Дейсвтие
        mgr1.load()

        # Проверки
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
    #проверка ограничений Settings
    def test_settings_constraints(self):
        s = Settings()
        # инн
        try:
            s.set_inn("123456789012")
            s.set_inn("123")
        except Exception as e:
            print("ИНН:", e)
        #счёт
        try:
            s.set_account("12345678901")
            s.set_account("123")
        except Exception as e:
            print("Счёт:", e)
        #корр.счёт
        try:
            s.set_corr_account("12345678901")
            s.set_corr_account("123")
        except Exception as e:
            print("Корр. счёт:", e)
        #бик
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

if __name__ == '__main__':
    unittest.main()
