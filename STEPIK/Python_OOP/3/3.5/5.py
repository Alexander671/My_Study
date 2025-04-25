## "–?!,.;"

class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words
    
    def __lt__(self, __o: object) -> bool:
        return len(self.lst_words) < len(__o.lst_words) 

    def __le__(self, __o: object) -> bool:
        return len(self.lst_words) <= len(__o.lst_words) 

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

lst_stich = []
for i in stich:
    st = i
    for j in "–?!,.;":
        st = st.replace(j, '')
    st = st.replace('  ', ' ')
    lst_stich.append(st)
    
lst_text = map(lambda x: StringText(x.split()), lst_stich)
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [ ' '.join(x.lst_words) for x in lst_text_sorted]
print(lst_text_sorted)