class SoftList(list):
    def __getitem__(self, key):
        if key > len(self) or abs(key) + 1 > len(self):
            return False
        else:
            return super().__getitem__(key)


sl = SoftList("python")
print(sl[0]) # 'p'
print(sl[-1]) # 'n'
print(sl[6])# False
print(sl[-7]) # False