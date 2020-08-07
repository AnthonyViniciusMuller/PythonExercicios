primeiro_termo = int(input("Qual é o primeiro termo: "))
razao = int(input("Qual é a razao: "))
numero_termos = int(input("Qual é o número de termos: "))
contador = 0
termo = primeiro_termo

print("=" * numero_termos * 3, end="")
print("\n")
while contador < numero_termos:
    termo = primeiro_termo + razao * contador
    print((termo), end=" ")
    contador += 1
