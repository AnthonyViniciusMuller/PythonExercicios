nome = str(input("Escreva uma frase: ")).strip().upper()
print("A letra {} aparece {} vezes na frase".format(nome[:1], nome.count(nome[:1])))
print("A letra {} aparece por último na posição {}".format(nome[:1], (nome.rfind(nome[:1])+1)))
