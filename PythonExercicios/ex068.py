import random

while True:
    pc = random.randint(0, 10)
    player = int(input("Digite um valor: "))
    choice = str(input("Escolha entre par ou ímpar[P/I]: ")).strip().upper()[0]
    while choice not in "PI":
        choice = str(input("Escolha entre par ou ímpar[P/I]: ")).strip().upper()[0]
    if (pc + player) % 2 == 0 and "P" in choice:
        print("Parabéns, você ganhou!")
        print(f"A soma foi {pc + player}")
    elif (pc + player) % 2 != 0 and "I" in choice:
        print("Parabéns, você ganhou!")
        print(f"A soma foi {pc + player}")
    else:
        print("Você perdeu")
        print(f"A soma foi {pc + player}")
        break