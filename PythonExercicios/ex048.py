contador = 0
soma = 0

for c in range(1, 500, 1):
    if c % 3 == 0 and c % 2 != 0:
        contador += 1
        soma += c

print("A soma dos {} numeros é {}".format(contador, soma))