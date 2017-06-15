from random import randrange
a = []
b = []
c = []

for x in range(10):
    a.append(randrange(1, 20))
    b.append(randrange(1, 20))

for x in a:
    if x in b and x not in c:
        c.append(x)

print(c)