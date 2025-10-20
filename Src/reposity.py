
"""
Репозиторий данных
"""
class reposity:
    def __init__(self):
        self.data = {
            "units": [],         #единицы измерения
            "groups": [],        #группы товаров
            "nomenclature": [],  #номенклатура
            "recipes": []        #рецепты
        }
    #добавление рецепта
    def add_recipe(self, recipe):
        self.data["recipes"].append(recipe)

    #получить все рецепты
    def get_recipes(self):
        return self.data["recipes"]

    #получить рецепт по имени
    def get_recipe_by_name(self, name):
        for recipe in self.data["recipes"]:
            if recipe.name == name:
                return recipe
        return None
