print("===============================\n 10 PRIMEIROS TERMOS DE UMA PA \n===============================\n")

primeiroTermo = int(input("Primeiro termo = "))
razao = int(input("Razão = "))
decimo = (primeiroTermo + (10 - 1) * razao) + razao

for c in range(primeiroTermo, decimo, razao):
    print("{} -> ".format(c), end = "")
print("ACABOU")