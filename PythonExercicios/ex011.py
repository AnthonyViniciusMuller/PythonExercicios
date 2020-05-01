largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
tamanho = largura*altura
print("A sua parede tem {} m²\nPara pintar sera necessário {} litros de tinta".format(tamanho, tamanho/2))