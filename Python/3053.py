
def embaralhar(pos_atual,moviment_atual):
    if moviment_atual == 1:
        if pos_atual == "A":
            pos_atual = "B"
        elif pos_atual == "B":
            pos_atual = "A"
    elif moviment_atual == 2:
        if pos_atual == "B":
            pos_atual = "C"
        elif pos_atual == "C":
            pos_atual = "B"
    elif moviment_atual == 3:
        if pos_atual == "A":
            pos_atual = "C"
        elif pos_atual == "C":
            pos_atual = "A"
    return pos_atual

total_mov = int(input())
pos_atual = str(input())

for _ in range(total_mov):

    moviment_atual = int(input())
    pos_atual = embaralhar(pos_atual,moviment_atual)

print(pos_atual)








