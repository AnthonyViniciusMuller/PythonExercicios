n1 = float(input("Digite um número: "))
n2 = float(input("Digite um segundo número: "))
option = 0

while option != 5:
    print("==============================")
    print(" [ 1 ] somar\n [ 2 ] multiplicar\n [ 3 ] maior\n [ 4 ] novos números\n [ 5 ] sair do programa")
    option = int(input("Escolha: "))
    if option == 1:
        print("A soma de {} e {} é {}".format(n1, n2, n1 + n2))
    elif option == 2:
        print("A multicação de {} e {} é {}".format(n1, n2, n1 * n2))
    elif option == 3:
        if n1 < n2:
            print("O maior entre {} e {} é {}".format(n1, n2, n2))
        else:
            print("O maior entre {} e {} é {}".format(n1, n2, n1))
    elif option == 4:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite um segundo número: "))
    elif option == 5:
        print("Encerrando programa")
    else:
        print("Opção inválida, tente novamente.")
