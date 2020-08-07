import random

numero_pc = random.randrange(0, 10)
numero_player = int(input("Adivinhe o número: "))

while numero_pc != numero_player:
    if numero_pc < numero_player:
        print("É um número menor, tente novamente...")
    elif numero_pc > numero_player:
        print("É um número maior, tente novamente...")

    numero_player = int(input("Adivinhe o número: "))

print("\n=========Parabéns=========")
print("Você acertou!")
