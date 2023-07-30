valor = float(input())
valor = valor * 100

cem = valor // 100
valor -= (cem * 100)
 
cinquenta = valor // 50
valor -= (cinquenta * 50)

vinte =  valor // 20
valor -= (vinte * 20)

dez = valor // 10
valor -= (dez * 10)

cinco = valor // 5
valor -= (cinco * 5)

dois = valor // 2
valor -= (dois * 2)

print("NOTAS:")
print(f"{cem//100} nota(s) de R$ 100.00")
print(f"{cinquenta//100} nota(s) de R$ 50.00")
print(f"{vinte//100} nota(s) de R$ 20.00")
print(f"{dez//100} nota(s) de R$ 10.00")
print(f"{cinco//100} nota(s) de R$ 5.00")
print(f"{dois//100} nota(s) de R$ 2.00")

um = valor // 1
valor -= um 
 
cinquenta_cents = valor // 0.50
valor -= (cinquenta_cents * 0.50)

vinte_e_cinco_cents =  valor // 0.25
valor -= (vinte_e_cinco_cents * 0.25)

dez_cents = valor // 0.10
valor -= (dez_cents * 0.10)

cinco_cents = valor // 0.5
valor -= (cinco_cents * 0.5)

um_cents = valor // 0.01
valor -= (um_cents * 0.01)

print("MOEDAS:")
print(f"{um//100} moeda(s) de R$ 1.00")
print(f"{cinquenta_cents//100} moeda(s) de R$ 0.50")
print(f"{vinte_e_cinco_cents//100} moeda(s) de R$ 0.25")
print(f"{dez_cents//100} moeda(s) de R$ 0.10")
print(f"{cinco_cents//100} moeda(s) de R$ 0.05")
print(f"{um_cents//100} moeda(s) de R$ 0.01")