h = {}
q = int(input('Сколько жанров '))
for i in range(q):
    g = input('Название жанра ')
    h[g] = ' '
movie = input('Название фильма ')
x = input('Жанр ')
if x in h:
    h[g] = movie
print(h)
