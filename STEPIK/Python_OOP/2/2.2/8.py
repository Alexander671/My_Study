from typing import List
class TreeObj: #  для описания вершин и листьев решающего дерева;
    def __init__(self, indx, value=None):
        self.index = indx # - проверяемый индекс (целое число);
        self.value = value # - значение с данными (строка);
        self.__left:TreeObj = None # - ссылка на следующий объект дерева по левой ветви (изначально None);
        self.__right:TreeObj = None # - ссылка на следующий объект дерева по правой ветви (изначально None).
    
    def get_left(self):
        return self.__left

    def set_left(self, left):
        self.__left = left

    def get_right(self):
        return self.__right

    def set_right(self, right):
        self.__right = right

    left = property(get_left,set_left)
    right = property(get_right, set_right)
    
class DecisionTree: # - для работы с решающим деревом в целом.
    @classmethod
    def predict(cls, root:TreeObj, x: List[int]) -> str: # - для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root.
        obj = root
        
        while obj:
            obj_next = cls.get_next(obj, x)
        
            if obj_next is None:
                break
            obj = obj_next
        return obj.value

    @classmethod
    def add_obj(cls, obj, node:TreeObj=None, left=True): # - для добавления вершин в решающее дерево (метод должен возвращать добавленную вершину - объект класса TreeObj);
        if node:                # если это корень
            if left:                    # далеее добавляем в зависимости от стороны потомка
                node.left = obj      
            else:                       
                node.right = obj
        return obj

    @classmethod
    def get_next(cls, obj, x):
        if x[obj.index] == 1:
            return obj.left
        else:
            return obj.right
root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
print(res)