class Layer:
    def __init__(self, next_Layer=None):
        self.name = 'Layer'
        self.next_Layer = next_Layer

    def __call__(self, layer):
        self.next_Layer = layer
        return layer

class Input(Layer): # - формирование входного слоя нейронной сети;
    def __init__(self, inputs):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs

class Dense(Layer): # - формирование полносвязного слоя нейронной сети.
    def __init__(self,inputs, outputs, activation):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs         # - число входов в слой;
        self.outputs = outputs       # - число выходов слоя (целые числа); 
        self.activation = activation # - функция активации (строка, например: 'linear', 'relu', 'sigmoid'). 
                                     # И в каждом объекте класса Dense также должен автоматически формироваться атрибут:

class NetworkIterator(Layer):
    def __iter__(self):
        self.value = self
        return self

    def __next__(self):
        if self.value.next_Layer == None:
            raise StopIteration
        else:
            self.value = self.value.next_Layer
        return self.value

nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu'))

n = 0
for x in NetworkIterator(nt):
    assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1
    
assert n == 2, "итератор перебрал неверное число слоев"