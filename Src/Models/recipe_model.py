class Ingredient:
    """
    Модель ингредиента рецепта.
    Содержит:
    - name: наименование ингредиента
    - amount: количество
    - unit: единица измерения
    """

    def __init__(self, name, amount, unit):
        #проверка входных данных при создании
        if not name or not isinstance(name, str):
            raise ValueError("Название ингредиента должно быть непустой строкой")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Количество ингредиента должно быть положительным числом")
        if not unit or not isinstance(unit, str):
            raise ValueError("Единица измерения должна быть строкой")
        self.__name = name
        self.__amount = amount
        self.__unit = unit

    #name
    @property
    def name(self):
        """Возвращает название ингредиента"""
        return self.__name
    @name.setter
    def name(self, value):
        """Устанавливает название ингредиента с проверкой"""
        if not value or not isinstance(value, str):
            raise ValueError("Название ингредиента должно быть непустой строкой")
        self.__name = value

    #amount
    @property
    def amount(self):
        """Возвращает количество ингредиента"""
        return self.__amount
    @amount.setter
    def amount(self, value):
        """Устанавливает количество ингредиента с проверкой"""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Количество ингредиента должно быть положительным числом")
        self.__amount = value

    #unit
    @property
    def unit(self):
        """Возвращает единицу измерения"""
        return self.__unit
    @unit.setter
    def unit(self, value):
        """Устанавливает единицу измерения с проверкой"""
        if not value or not isinstance(value, str):
            raise ValueError("Единица измерения должна быть строкой")
        self.__unit = value

class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.steps = []
        self.cook_time = 0

    def add_ingredient(self, name, amount, unit):
        ing = Ingredient(name, amount, unit)
        self.ingredients.append(ing)

    def add_step(self, step):
        self.steps.append(step)

    def set_cook_time(self, minutes):
        self.cook_time = minutes
