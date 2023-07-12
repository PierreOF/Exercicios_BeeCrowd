

while True:
    x,y = map(int,input().split())
    lista = []
    soma = 0

    if x <= 0 or y <= 0:
        break
    elif x > y:
        for num in range(y,x+1):
            soma += num
            lista.append(num)
    else:
        for num in range(x,y+1):
            soma += num
            lista.append(num)

    
    print(f"{' '.join(str(elemento) for elemento in lista)} Sum={soma}")