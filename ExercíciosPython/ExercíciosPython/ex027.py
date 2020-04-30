nome = str(input("Qual é o seu nome: ")).strip()
print("Seu primeiro nome é {}".format(nome[:nome.find(' ')]))
print("Seu primeiro nome é {}".format(nome[(nome.rfind(' '))+1:]))
