# множественное наследование со сложной структурой 
# проверка алгоритма MRO
class A: pass
class A1(A): pass
class A2: pass
class A3: pass
class B1(A1): pass
class B2(A2): pass
class B3(A1): pass
class C1(B1, B3): pass
class C2(B1,B2): pass
class C3(B2): pass
class D(C1, C2, C3): pass
print(D.__mro__)