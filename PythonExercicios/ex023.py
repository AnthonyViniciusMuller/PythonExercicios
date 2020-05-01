n1 = int(input("Digite um número: "))
print("Analizando o número {}".format(n1))

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print(" Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}".format(u, d, c, m))