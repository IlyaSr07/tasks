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
            for i1 in range(width):
                self.map[v][h] = '*'
                h = h+1
        else:
            if v == 0:
                v=v+1
            for i2 in range(width):
                self.map[v][h] = '*'
                self.map[v-1][h] = '*'
                h = h+1
        h = randint(0, (length-1))
        if h<2:
          h = 2
        print(v, h)
        for i3 in range(length):
          self.map[v][h] = '*'
          self.map[v][h-1] = '*'
          self.map[v][h-2] = '*'
          v = v+1

    def showmap(self):
        for part in self.map:
            print(part)
x = CityMap()
x.drawmap(8, 5)
x.showmap()
