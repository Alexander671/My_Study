# Дополните приведенный код так, чтобы в переменной result хранился словарь,
# в котором для каждого символа строки text будет подсчитано 
# количество его вхождений.

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'


result = {}
for num in text:
    result[num] = result.get(num, 0) + 1