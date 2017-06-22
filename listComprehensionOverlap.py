from random import sample
a = sample(range(100), 20)
b = sample(range(100), 22)
c = []
print(a)
print(b)
for x in a:
    if x in b:
        c.append(x)

print(c)