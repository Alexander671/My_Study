class SingletonFive:
    __instance = []
    def __new__(cls, args):
        if len(cls.__instance) < 5:
            cls.__instance.append(super().__new__(cls))
        return cls.__instance[-1] 

objs = [SingletonFive(str(n)) for n in range(10)]