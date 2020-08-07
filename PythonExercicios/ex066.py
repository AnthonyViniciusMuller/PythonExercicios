soma = 0
while True:
    n1 = int(input("Digite 999 para parar: "))
    if n1 == 999:
        break
    soma += n1

print("A soma de todos os números foi {}.".format(soma))