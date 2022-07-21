class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name # - название ингредиента (строка);
        self.volume = volume # - объем ингредиента в рецепте (вещественное число);
        self.measure = measure # - единица измерения объема ингредиента (строка), например, литр, чайная ложка, грамм, штук и т.д.;

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    def __init__(self, *args):
        self.list_recipe = list(args)
    
    def add_ingredient(self, ing): # - добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец);
        self.list_recipe.append(ing)

    def remove_ingredient(self, ing): # - удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;
        self.list_recipe.remove(ing)

    def get_ingredients(self): #- получение кортежа из объектов класса Ingredient текущего рецепта.
        return tuple(self.list_recipe)

    def __len__(self):
        return len(self.list_recipe)

recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3
print(Ingredient("Масло", 100, "гр"))
print(n)