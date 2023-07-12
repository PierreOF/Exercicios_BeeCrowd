
dia_inicio = input().split()
dia_i = int(dia_inicio[1])

hora_i , minuto_i , segundo_i = list(map(int,input().split(":")))

dia_fim = input().split()
dia_f = int(dia_fim[1])

hora_f , minuto_f , segundo_f = list(map(int,input().split(":")))

dia = dia_f - dia_i 
hora = hora_f - hora_i
minuto = minuto_f - minuto_i
segundo = segundo_f - segundo_i

if segundo < 0:
    segundo += 60
    minuto -= 1 
if minuto < 0:
    minuto += 60
    hora -= 1
if hora < 0:
    hora += 24
    dia -= 1 

print(f"{dia} dia(s)")
print(f"{hora} hora(s)")
print(f"{minuto} minuto(s)")
print(f"{segundo} segundo(s)")
