def ordenar_soma_time(qtd, numero_time):
    soma_tem = 0
    for i in range(qtd - 1, 0, -1):
        for j in range(i):
            if numero_time[j][0] > numero_time[j+1][0]:
                numero_time[j], numero_time[j+1] = numero_time[j+1], numero_time[j]
                soma_tem += numero_time[j][1] + numero_time[j+1][1]
    return soma_tem

while True:
    try:
        qtd_caixas = int(input())
        numeros_caixas = map(int,input().split())
        tempo_caixas = map(int,input().split())
        numero_time = [[x, y] for x, y in zip(numeros_caixas, tempo_caixas)]
        tempo_de_troca = ordenar_soma_time(qtd_caixas, numero_time)
        print(tempo_de_troca)
    except EOFError:
        break
