from math import *

n = input()
valores = list(map(int,input().split()))

menor_valor = min(valores)
posicao = valores.index(menor_valor)

for i in range(int(n)):
    if valores[i] < menor_valor:
        menor_valor = valores[i]
        posicao = i
        
print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")


