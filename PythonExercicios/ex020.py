import random
pessoa1 = str(input("Primeira pessoa: "))
pessoa2 = str(input("Segunda pessoa: "))
pessoa3 = str(input("Terceira perssoa: "))
pessoas = [pessoa1, pessoa2, pessoa3]
random.shuffle(pessoas)

print("A ordem de apresentação será {}".format(pessoas))
