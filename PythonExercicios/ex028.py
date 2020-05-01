import random

n1 = random.randint(0, 3)
n2 = int(input("Digite um valor de 0 a 3: "))
if n1 == n2:
    print("Voce acertou!")
else:
    print("Você errou. O número certo era {}".format(n1))