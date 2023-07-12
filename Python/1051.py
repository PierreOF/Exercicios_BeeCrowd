salario = float(input())

if salario <= 2000:
    print("Isento")

elif salario > 2000 and salario <= 3000:
    tributavel = salario - 2000
    imposto = (tributavel * 0.08)
    print(f"R$ {imposto:.2f}")
elif salario > 3000 and salario <= 4500:
    tributavel = salario - 3000 
    imposto = (tributavel * 0.18) + (1000 * 0.08)
    print(f"R$ {imposto:.2f}")
elif salario > 4500:
    tributavel = salario - 4500 
    imposto = (tributavel * 0.28) + (1000 * 0.08) + (1500 * 0.18)
    print(f"R$ {imposto:.2f}")
