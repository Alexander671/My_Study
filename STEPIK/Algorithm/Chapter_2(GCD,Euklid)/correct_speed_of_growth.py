# Упорядочите данные функции по возрастанию скорости роста
# (сверху — медленнее всего растущая функция, снизу — быстрее всего растущая).
#
#
#
#

from sympy import log, sqrt, Symbol, limit, oo,  Pow, factorial, pprint

class CompareLimits:
    def __init__(self, obj):
        self.obj = obj

    def __lt__(self, other):
        return limit((self.obj/other.obj), n, oo) == 0

    def __gt__(self, other):
        return limit((self.obj/other.obj), n, oo) == oo


n = Symbol('n')
functions = list(map(lambda x: CompareLimits(x), 
            [log((log(n, 2)), 2), 
             sqrt(log(n, 4)),
             log(n, 3),
             Pow(log(n, 2), 2),
             sqrt(n),
             (n/log(n,5)),
             Pow(3, log(n, 2)),
             log(factorial(n), 2),
             Pow(n, log(n, 2)),
             Pow(n, 2),
             Pow(7, log(n, 2)),
             Pow(2, n),
             Pow(4, n),
             Pow(2, 3 * n),
             Pow(n, sqrt(n)),
             factorial(n),
             Pow(2, Pow(2, n)),
             Pow(log(n, 2), log(n, 2))]))

sorted_functions = sorted(functions)
for func in sorted_functions:
    pprint(func.obj)
    print('-------------------------------------')