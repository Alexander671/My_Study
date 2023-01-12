class Goods:
    '''
    LalaLand
    '''
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024

setattr(Goods, 'price', 2048)
setattr(Goods, 'inflation', 100)
g = Goods()
print(Goods.__doc__)