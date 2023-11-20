import random

nombres = []
for _ in range(100_000):
    # print(random.randint(1, 99) ** 2)
    nombres += [random.randint(1, 99) ** 2]
print(nombres)