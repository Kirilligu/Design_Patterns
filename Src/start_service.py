from Src.reposity import reposity
from Src.Models.unit_model import unit_model
from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.recipe_model import Recipe


class start_service:
    def __init__(self):
        self.repo = reposity()
        self.repo.data["units"] = []
        self.repo.data["groups"] = []
        self.repo.data["nomenclature"] = []
        self.repo.data["recipes"] = []

    #ед.измерения
    def create_units(self):
        gram = unit_model("грамм", 1.0)
        kilogram = unit_model("килограмм", 1000.0, base_unit=gram)
        piece = unit_model("штука", 1.0)

        self.repo.data["units"].extend([gram, kilogram, piece])
        return gram, kilogram, piece

    #группы товаров
    def create_groups(self):
        fruits = group_model("Фрукты")
        vegetables = group_model("Овощи")
        sweets = group_model("Сладости")

        self.repo.data["groups"].extend([fruits, vegetables, sweets])
        return fruits, vegetables, sweets

    #номенклатура
    def create_nomenclature(self, units, groups):
        gram, kilogram, piece = units
        fruits, vegetables, sweets = groups
        apple = nomenclature_model("Яблоко", "Свежее красное яблоко", piece, fruits)
        carrot = nomenclature_model("Морковь", "Свежая морковь", piece, vegetables)
        sugar = nomenclature_model("Сахар", "Сахар-песок белый", gram, sweets)
        self.repo.data["nomenclature"].extend([apple, carrot, sugar])
        return apple, carrot, sugar

    def create_receipts(self, apple, carrot, sugar):
        #Вафли хрустящие
        waffles = Recipe("Вафли хрустящие в вафельнице")
        waffles.add_ingredient("Пшеничная мука", 100, "г")
        waffles.add_ingredient("Сахар", 80, "г")
        waffles.add_ingredient("Сливочное масло", 70, "г")
        waffles.add_ingredient("Яйца", 1, "шт")
        waffles.add_ingredient("Ванилин", 5, "г")
        waffles.add_step("Подготовьте все продукты.")
        waffles.add_step("Масло растопите в сотейнике на маленьком огне или на водяной бане.")
        waffles.add_step("Добавьте сахар и перемешайте венчиком до растворения.")
        waffles.add_step("Добавьте яйцо и перемешайте до однородности.")
        waffles.add_step("Всыпьте муку и ванилин, перемешайте до гладкого теста.")
        waffles.add_step("Разогрейте вафельницу, выкладывайте тесто по столовой ложке.")
        waffles.add_step("Выпекайте до золотистого цвета, аккуратно снимайте вафли лопаткой.")
        waffles.set_cook_time(20)

        #Шарлотка с яблоками
        charlotte = Recipe("Шарлотка с яблоками")
        charlotte.add_ingredient(apple.name, 500, "г")
        charlotte.add_ingredient("Яйца", 3, "шт")
        charlotte.add_ingredient(sugar.name, 150, "г")
        charlotte.add_ingredient("Пшеничная мука", 180, "г")
        charlotte.add_ingredient("Разрыхлитель теста", 1, "ч. ложка")
        charlotte.add_ingredient("Ванильный сахар", 10, "г")
        charlotte.add_ingredient("Сливочное масло", 20, "г")
        charlotte.add_step("Подготовьте все продукты, яблоки очистите и нарежьте дольками.")
        charlotte.add_step("Взбейте яйца с сахаром и ванильным сахаром до пышной массы.")
        charlotte.add_step("Просейте муку с разрыхлителем и аккуратно добавляйте в смесь.")
        charlotte.add_step("Форму смажьте маслом и слегка присыпьте мукой.")
        charlotte.add_step("Выложите половину теста, затем яблоки, сверху оставшееся тесто.")
        charlotte.add_step("Разогрейте духовку до 180°C и выпекайте 30-35 минут.")
        charlotte.add_step("Проверьте готовность шпажкой, дайте остыть, подавайте при желании с сахарной пудрой.")
        charlotte.set_cook_time(45)

        self.repo.data["recipes"].extend([waffles, charlotte])

        return [waffles, charlotte]

    def create(self):
        units = self.create_units()
        groups = self.create_groups()
        apple, carrot, sugar = self.create_nomenclature(units, groups)
        self.create_receipts(apple, carrot, sugar)
        return True
