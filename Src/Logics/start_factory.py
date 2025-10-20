from Src.Models.unit_model import unit_model
from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import nomenclature_model


class start_factory:
    def __init__(self):
        # единицы измерения
        self.units = [
            unit_model("Килограмм", 1.0),
            unit_model("Литр", 1.0),
            unit_model("Штука", 1.0)
        ]

        # группы
        self.groups = [
            group_model(name="Продукты питания"),
            group_model(name="Бытовая химия")
        ]

        # номенклатура
        self.nomenclatures = [
            nomenclature_model(
                name="Мука пшеничная",
                full_name="Мука пшеничная высшего сорта 1 кг",
                unit=self.units[0],
                group=self.groups[0]
            ),
            nomenclature_model(
                name="Сахар-песок",
                full_name="Сахар-песок белый кристаллический 1 кг",
                unit=self.units[0],
                group=self.groups[0]
            ),
            nomenclature_model(
                name="Мыло хозяйственное",
                full_name="Мыло хозяйственное 72%, брусок 200 г",
                unit=self.units[2],
                group=self.groups[1]
            ),
        ]

    def get_all(self):
        """Вернуть все сущности в виде словаря"""
        return {
            "units": self.units,
            "groups": self.groups,
            "nomenclatures": self.nomenclatures
        }
