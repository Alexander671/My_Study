class RenderList:
    def __init__(self, type):
        self.type_list = type


    def __call__(self, values):
        rows = '\n'.join([f'<li>{i}</li>' for i in values])
        return f'<{self.type_list}>\n{rows}\n</{self.type_list}>'


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst) # возвращается многострочная строка с соответствующей HTML-разметкой
lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
print(html)