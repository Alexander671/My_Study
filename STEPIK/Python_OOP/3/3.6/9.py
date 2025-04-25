class Dimensions:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self) -> int:
        current_hash = hash((self.a, self.b, self.c))
        return current_hash

    def __setattr__(self, __name: str, __value) -> None:
        if __value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        else:
            object.__setattr__(self, __name, __value)
text = input()
lst_dims = map(lambda x: Dimensions(*list(map(lambda y: float(y), x.split()))), text.split(';'))
lst_dims = sorted(lst_dims, key=hash)
