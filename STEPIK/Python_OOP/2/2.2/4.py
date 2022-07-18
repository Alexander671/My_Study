class Car:
    def __init__(self, model):
        self.__model = model

# - модель автомобиля - это строка;
# - длина строки модели должна быть в диапазоне [2; 100].
    def get_model(self):
        return self.__model 

    def set_model(self, model):
        if type(model) == str:
            if 2 <= len(str) <= 100:
                self.__model = model

    model = property(get_model, set_model)