class RandomPassword:
    def __init__(self, psw_chars, min_len, max_len):
        self.psw_chars = psw_chars
        self.min_len = min_len
        self.max_len = max_len


    def __call__(self):
        return self.psw_chars[:self.min_len]
        

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd(), rnd(), rnd()]
print(lst_pass)