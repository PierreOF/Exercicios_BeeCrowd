


x = int(input())
y = int(input())

soma_impares = 0

if x < y:
    for num in range(x+1,y):
        if num % 2 != 0:
            soma_impares += num
else:
    for num in range(y+1,x):
        if num % 2 != 0:
            soma_impares += num

print(soma_impares)