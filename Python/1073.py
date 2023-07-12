

valor = int(input())


for num in range(1,valor+1):
    if num % 2 == 0:
        num_elevado = num ** 2
        print(f"{num}^2 = {num_elevado}")

