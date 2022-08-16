class Validator:
    def _is_valid(self, data): 
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) == float:
            return self.min_value <= value <= self.max_value 
        return False