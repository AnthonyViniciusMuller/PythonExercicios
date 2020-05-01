dias = int(input("Digite quantos dias você usou o carro: "))
distancia = float(input("Quantos Km você dirigiu: "))
preco = (dias*60) + (distancia*0.15)
print("O valor a ser pago é {} reais".format(preco))
