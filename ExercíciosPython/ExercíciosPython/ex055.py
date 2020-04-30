menorPeso = 0
maiorPeso = 0

peso = float(input("Qual é o seu peso: "))
menorPeso = peso

for c in range(5):
    peso = float(input("Qual é o seu peso: "))
    if maiorPeso < peso:
        maiorPeso = peso
    if menorPeso > peso:
        menorPeso = peso

print("O maior peso foi {:.2f} kilos e o menor foi {:.2f} kilos".format(maiorPeso, menorPeso))