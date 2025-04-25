class Model:
    def query(self, *args, **kwargs):
        self.queries = kwargs

    def __str__(self) -> str:
        if hasattr(self, 'queries'):
            list_of_value = ', '.join([ f'{str(i)} = {str(j)}' for i, j in self.queries.items()])
            return f"Model: {list_of_value}"
        else:
            return "Model"

model = Model()
model.query(id=1, fio='Sergey', old=33)

print(model)