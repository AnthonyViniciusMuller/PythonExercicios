n1 = int(input("Digite um número: "))
contador = 0

for c in range(1, n1 + 1, 1):
    if n1 % c == 0:
        contador += 1

if contador == 2:
    print("É um número primo")
else:
    print("Não é um número primo")