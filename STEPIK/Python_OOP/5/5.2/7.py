def get_loss(w1, w2, w3, w4):
    x  = 10 * w1
    try:
        res = x // w2
    except:
        return "деление на ноль"
    else:
        y = res - 5 * w2 * w3 + w4
        return y