frase = str(input("Digite uma frase: ")).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print("Você digitou: {}\nAo contraria: {}".format(junto, inverso))
if inverso == junto:
    print("A Frase é um palíndromo")
