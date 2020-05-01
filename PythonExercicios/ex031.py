distancia = float(input("Qual é a distância da viagem: "))

if distancia > 200:
    valor = distancia * 0.45
else:
    valor = distancia * 0.5

print("O valor a ser pago, em uma viagem de {}Km, é de {} reais")