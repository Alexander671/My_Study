def cakes(recipe, available):
    return int(min(available.get(k, 0)/recipe[k] for k in recipe))

book = ({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
print(cakes(*book))

book = ({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000})
print(cakes(*book))
