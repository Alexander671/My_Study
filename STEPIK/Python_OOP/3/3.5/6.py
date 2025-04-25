s = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""

class Morph:
    def __init__(self, *args):
        self.words = list(args)


    def add_word(self, word): # - добавление нового слова (если его нет в списке слов объекта класса Morph);
        self.words.append(word)

    def get_words(self): #- получение кортежа форм слов.
        return tuple(self.words)

    def __eq__(self, __o: object) -> bool:
        return __o.lower() in self.words



dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.splitlines()]
text = input()
lst_stich = []
for i in text:
    st = i
    for j in "–?!,.;":
        st = st.replace(j, '')
    st = st.replace('  ', ' ')
    lst_stich.append(st)

changed = ''.join(lst_stich).split()
sum = 0
for i in changed:
    for j in dict_words:
        if j == i:
            sum += 1
print(sum)



print(dict_words[0] != 'связи')
