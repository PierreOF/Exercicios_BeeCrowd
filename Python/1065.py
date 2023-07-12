

valores_pares = 0

for _ in range(0,5):
    valor = int(input())
    if valor % 2 == 0:
        valores_pares += 1

print(f"{valores_pares} valores pares")