from abc import ABC, abstractmethod


class CountryInterface(ABC):
    def __init__(self, name, population, square):
        self.__name = name # - абстрактное свойство (property), название страны (строка);
        self.__population = population # - абстрактное свойство (property), численность населения (целое положительное число);
        self.__square = square # - абстрактное свойство (property), площадь страны (положительное число);
    
    @property
    @abstractmethod
    def name(self, ):
        return self.__name

    @name.setter
    @abstractmethod
    def name(self, v):
        self.__name = v

    @property
    @abstractmethod
    def population(self, ):
        return self.__population

    @population.setter
    @abstractmethod
    def population(self, v):
        self.__population = v

    @property
    @abstractmethod
    def square(self, ):
        return self.__square

    @square.setter
    @abstractmethod
    def square(self, v):
        self.__square = v
    
    @abstractmethod
    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"

class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.__name = name # - абстрактное свойство (property), название страны (строка);
        self.__population = population # - абстрактное свойство (property), численность населения (целое положительное число);
        self.__square = square # - абстрактное свойство (property), площадь страны (положительное число);
    
    @property
    def name(self, ):
        return self.__name

    @name.setter
    def name(self, v):
        self.__name = v

    @property
    def population(self, ):
        return self.__population

    @population.setter
    def population(self, v):
        self.__population = v

    @property
    def square(self, ):
        return self.__square

    @square.setter
    def square(self, v):
        self.__square = v
    
    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"
