

valores = list(map(int,input().split()))

if valores[0] == valores[1]:
    valor_final = 24
elif valores[0] > valores[1]:
    valor1 = 24 - valores[0]
    valor_final = valor1 + valores[1]
else :
    valor_final = valores[1] - valores[0]
    
print(f"O JOGO DUROU {valor_final} HORA(S)")
