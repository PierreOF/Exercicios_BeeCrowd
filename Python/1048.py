
salario = float(input())

def saida(salary,porcentagem):
    reajuste = ((salary * porcentagem) / 100)
    novo_salario = (salary + reajuste)

    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {porcentagem} %")


if salario <= 400:
    saida(salario,15)
elif salario > 400 and salario <= 800:
    saida(salario,12)
elif salario > 800 and salario <= 1200:
    saida(salario,10)
elif salario > 1200 and salario <= 2000:
    saida(salario,7)
elif salario > 2000:
    saida(salario,4)