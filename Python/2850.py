while True:
    try:
        entrada = str(input())
        
        if entrada == "esquerda":
            fala = "ingles"
        elif entrada == "direita":
            fala = "frances"
        elif entrada == "nenhuma":
            fala = "portugues"
        elif entrada == "as duas":
            fala = "caiu"
        
        print(fala)
        
    except EOFError:
        break
