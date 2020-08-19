numero = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite mais um número: ")), int(input("Digite o último número: ")))
print("===" * 15)
print(f"O número 9 apareceu {numero.count(9)} veze(s)")
for c in range(0, len(numero)):
    if numero[c] == 3:
        print(f"O número 3 aparece na posição {c}")
for c in range(0, len(numero)):
    if numero[c] % 2 == 0:
        print(f"O número {numero[c]} é par")