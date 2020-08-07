n1 = int(input("Digite um número: "))
fatorial = 1

print("{}! = ".format(n1), end="")
for c in range(1, n1 + 1):
    fatorial *= c
    print("{}".format(c), end="")
    if c != n1:
        print(" x ", end="")
    else:
        print(" = ", end="")

print("{}".format(fatorial), end="")