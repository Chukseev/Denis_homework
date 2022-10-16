import math
x = 2
y = 3
u1 = math.pow(x,2) + 2 * math.pow(y, 2) * x - 4
u2 = math.pow(y, 3) - (4 * x * y) + math.pow(x, 2)
print('Выражение u1 =', u1)
print('Выражение u1 =', u2)
if u1 == u2:
    print('Выражение u1 равняется выражению u2')
elif u1 > u2:
    print('Выражение u1 больше выражения u2')
else:
    print('Выражение u2 больше выражения u1')
