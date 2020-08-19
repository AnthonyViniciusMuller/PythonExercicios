produtos = ("Lapis", '1,75', 'Borracha', '2,00', 'Caderno', '15.00', 'Estojo', '25.00', 'Transferidor', '4,70', 'Compasso', '9,99', 'Canetas', '22,20', 'Mochila', '120.32', 'Livro', '34,90')

for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f"{produtos[c]}", end='')
        print("." * (20 - len(produtos[c])), end='')
        print(f"R$ {produtos[c + 1]:>6}")
