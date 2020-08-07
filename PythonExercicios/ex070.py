contador_mil = 0
barato_name = " "
barato_preco = 0
valor_total = 0
while True:
    nome = str(input("Qual é o nome do produto: "))
    produto = float(input("Qual é o valor do produto: "))
    if barato_preco == 0:
        barato_preco = produto
    elif barato_preco > produto:
        barato_preco = produto
        barato_name = nome
    if produto >= 1000:
        contador_mil += 1
    valor_total += produto
    escolha = str(input("Deseja continuar[S/N]: ")).strip().upper()[0]
    while escolha not in "SN":
        escolha = str(input("Invalido! Deseja continuar[S/N]: ")).strip().upper()[0]
    if escolha in "N":
        break
print(f"O valor total foi de {valor_total} reais, houveram {contador_mil} produtos que custaram mil ou mais, e o produto mais barato foi {barato_name} por {barato_preco}.")
