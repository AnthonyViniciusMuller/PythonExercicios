palavras = ('aprender', 'programar', 'Linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programar', 'futuro')

while True:
    for c in range(0, len(palavras)):
        print(f"\nA palavra {palavras[c]} tem as vogais", end=' ')
        for v in palavras[c]:
            if v in 'aeiou':
                print(v, end=' ')

    break
