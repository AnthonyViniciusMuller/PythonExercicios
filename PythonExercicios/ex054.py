dataNasc = ''
cJovens = 0
cAdultos = 0

for c in range(5):
    dataNasc = int(input("Em que ano você nasceu: "))
    if 2020 - dataNasc < 18:
       cJovens += 1
    else:
        cAdultos += 1
print("Tivemos {} pessoas maiores de idade. \nTivemos {} pessoas menores de idade.".format(cAdultos, cJovens))