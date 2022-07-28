import sys


class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return bool(self.score)

    def __len__(self):
        return self.score

# преобразование строк к заданному формату
lst_in = list(map(str.strip, sys.stdin.readlines()))
players = list(map(lambda x: Player(*[x.split(';')[0], int(x.split(';')[1]), int(x.split(';')[2])]), lst_in))
players_filtered = list(filter(lambda x: len(x) > 0, players))
print(list(players_filtered))