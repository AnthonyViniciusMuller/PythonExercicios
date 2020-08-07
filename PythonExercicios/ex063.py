n1 = 0
n2 = 1
contador = 0
numero_termos = int(input("Quantos termos serão exibidos: "))

while contador < numero_termos / 2:
    contador += 1
    print(n1, end=" ")
    print(n2, end=" ")
    n1 += n2
    n2 += n1