soma = 0
n1 = int(input("Digite um valor: "))

while n1 != 999:
    soma += n1
    n1 = int(input("Digite um valor: "))

print("A soma de todos os números foi {}.".format(soma))