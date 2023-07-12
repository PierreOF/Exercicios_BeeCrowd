v_par = 0 
v_impar = 0
v_positivo = 0
v_negativo = 0

for _ in range(0,5):
    valor = int(input())
    if valor % 2 == 0:
        v_par += 1 
    if valor % 2 != 0:
        v_impar += 1
    if valor > 0 :
        v_positivo += 1 
    if valor < 0:
        v_negativo += 1

print(f"{v_par} valor(es) par(es)")
print(f"{v_impar} valor(es) impar(es)")
print(f"{v_positivo} valor(es) positivo(s)")
print(f"{v_negativo} valor(es) negativo(s)")
