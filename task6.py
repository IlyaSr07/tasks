from random import randint

class CityMap:
    def __init__(self):
        self.map = []

    def drawmap(self, length, width):
        h = 0
        v = 0
        for i in range(length):
            f = []
            for b in range(width):
                f.append('@')
            self.map.append(f)
        v = randint(0, (length-1))
        if randint(1, 2) == 1: #h roads
            for i in range(width):
                self.map[v][h] = '*'
                h = h+1
        else:
            if v == 0:
                v=v+1
            for i in range(width):
                self.map[v][h] = '*'
                self.map[v-1][h] = '*'
                h = h+1

    def showmap(self):
        for part in self.map:
            print(part)
x = CityMap()
x.drawmap(8, 5)
x.showmap()
