from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self): 
        return "Базовый класс Model"

class ModelForm(Model):
    unique_id = 0
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.__class__.unique_id
        self.__class__.unique_id += 1

    def get_pk(self): 
        return self._id