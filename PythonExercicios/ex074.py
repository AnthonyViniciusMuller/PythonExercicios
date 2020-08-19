import random

numeros = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

print(numeros)
print(sorted(numeros)[:1])
print(sorted(numeros)[-1:])