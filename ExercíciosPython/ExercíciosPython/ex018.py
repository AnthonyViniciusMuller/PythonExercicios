import math
angulo = float(input("Digite o ângulo: "))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))

print("Seno: {:.2f}\nTangente: {:.2f}\nCosseno{:.2f}".format(seno, tangente, cosseno))