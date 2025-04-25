class Translator:
    dict_words = {}
    def add(self, eng, rus):
        self.dict_words.setdefault(eng, []).append(rus)
    
    def remove(self, eng):
        del self.dict_words[eng]

    def translate(self, eng):
        return self.dict_words[eng]

tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(*tr.translate('go'))

