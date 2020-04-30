soma = 0

print("Serão requisitados seis números\n")
for c in range(0, 7, 1):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        soma += n

print("A soma dos números pares é {}".format(soma))