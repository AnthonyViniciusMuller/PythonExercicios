primeiro_termo = int(input("Qual é o primeiro termo: "))
razao = int(input("Qual é a razao: "))
numero_termos = int(input("Qual é o número de termos: "))
contador = 0
termo = primeiro_termo
soma_numero_termos = 0

print("=" * numero_termos * 3, end="")
print("\n")
while contador < numero_termos:
    soma_numero_termos += 1
    termo = primeiro_termo + razao * contador
    print((termo), end=" ")
    contador += 1
    if contador == numero_termos:
        numero_termos += int(input("\nQuantos termos você quer a mais: "))

print("Fora feitas {} PAs".format(soma_numero_termos))
