valores = list(map(int,input().split()))

valores_input = valores.copy()
valores.sort()
valores_ord = valores

for v in valores_ord:
    print(v)

print("")

for v1 in valores_input:
    print(v1)