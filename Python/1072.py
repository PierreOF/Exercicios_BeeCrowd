
valor = int(input())
v_in = 0
v_out = 0

for num in range(0,valor):
    valores = int(input())
    if valores >= 10 and valores <= 20:
        v_in += 1
    else:
        v_out += 1 

print(f"{v_in} in")
print(f"{v_out} out")
 
    


