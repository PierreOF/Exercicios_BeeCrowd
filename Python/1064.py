valores_positivos = 0
soma_positivos = 0

for i in range(0,6):
    valor = float(input())
    if valor > 0:
        valores_positivos += 1
        soma_positivos += valor
     
media = soma_positivos / valores_positivos 
print(f"{valores_positivos} valores positivos")
print(f"{media:.1f}")


