entrada = input()

for _ in range(int(entrada)):
    texto_entrada = input()
    metade_do_texto = int(len(texto_entrada) / 2)
    primeira_criptografia = ""
    for l in texto_entrada:
        if l.isalpha():
            letra_unicode = (ord(l) + 3)
            letra_alpha = chr(letra_unicode)
            primeira_criptografia += str(letra_alpha)
        else:
            primeira_criptografia += str(l)

    segunda_criptografia = primeira_criptografia[::-1]
    metade = segunda_criptografia[metade_do_texto:]
    metade_deslocada = ""
    for c in metade:
        letra_unicode = (ord(c) - 1)
        letra_alpha = chr(letra_unicode)
        metade_deslocada += str(letra_alpha)

    terceira_criptografia = segunda_criptografia[0:metade_do_texto] + metade_deslocada
    print(terceira_criptografia)


