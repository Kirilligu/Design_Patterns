class Ingredient:
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit
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
