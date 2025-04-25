from collections import Counter  # словарь в котором для каждого объекта поддерживается счетчик

class Tree:
    dict_result = {}
    def __init__(self, value, freq, code=""):
        self.value = value
        self.freq = freq
        self.code = code

    def __add__(self, other):
        self.node = Tree(self.value + other.value, self.freq + other.freq)
        self.node.left = self
        self.node.right = other
        return self.node

    def walk(self, lst=[]):
        if len(self.value) == 1:
            self.dict_result[self.value] = self.code
            self.node = None

        else:
            self.left.code = self.code + '0'
            self.left.walk()
            self.right.code += self.code + '1'
            self.right.walk()

def huffman_encode(s):  # функция кодирования строки в коды Хаффмана
    code = Counter(s)
    elements = list(map(lambda x: Tree(*x), code.items()))
    while len(elements) >= 2:
        elem1 = min(elements, key=lambda x: x.freq)
        elements.remove(elem1)
        elem2 = min(elements, key=lambda x: x.freq)
        elements.remove(elem2)
        elements.append(elem1 + elem2)
    last_element = elements[0]
    last_element.walk()
    
    if len(code) == 1:
        return {s[0] : 0}

    return last_element.dict_result  # возвращаем словарь символов и соответствующих им кодов

def main():
    s = input()  # читаем строку длиной  до 10**4
    code = huffman_encode(s)  # кодируем строку
    encoded = "".join(str(code[ch]) for ch in s)  # отобразим закодированную версию, отобразив каждый символ
                                             # в соответствующий код и конкатенируем результат
    print(len(code), len(encoded))  # выведем число символов и длину закодированной строки
    for ch in sorted(code): # обойдем символы в словаре в алфавитном порядке с помощью функции sorted()
        print("{}: {}".format(ch, code[ch]))  # выведем символ и соответствующий ему код
    print(encoded)  # выведем закодированную строку

if __name__ == "__main__":
    main()