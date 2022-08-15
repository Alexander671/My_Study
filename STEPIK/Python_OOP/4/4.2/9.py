class IteratorAttrs:
    def __iter__(self): # - для получения объекта-итератора (в данном случае - это сам объект self)
        for x in self.__dict__.items():
            yield x


class SmartPhone(IteratorAttrs):
    def __init__(self,model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory

phone = SmartPhone('model', 'size', 'memory')
for attr, values in phone:
    print(attr, values)