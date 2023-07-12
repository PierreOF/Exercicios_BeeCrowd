
DDD = int(input())

digitos = [61,71,11,21,32,19,29,31]
destinos = ["Brasilia","Salvador","Sao Paulo","Rio de Janeiro","Juiz de Fora","Campinas","Vitoria","Belo Horizonte"]

if DDD in digitos:
    print(destinos[digitos.index(DDD)])
else:
    print("DDD nao cadastrado")
        