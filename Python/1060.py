r = 0
valores_positivos = 0
while r < 6:
    numero = float(input())
    if numero > 0:
        valores_positivos += 1
    r += 1 

print(f"{valores_positivos} valores positivos")
