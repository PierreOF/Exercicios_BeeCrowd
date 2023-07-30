from math import *

quntd_numeros = int(input())
numeros = list(map(int,input().split()))

menor_numero_possivel = max(numeros)+1
numeros_corretos = 0
while numeros_corretos < len(numeros):
    for y in numeros:
        if gcd(y,menor_numero_possivel) == 1:
            numeros_corretos += 1     

    menor_numero_possivel += 1 
    
print(menor_numero_possivel-1)