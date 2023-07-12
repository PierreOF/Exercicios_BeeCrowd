

lados = list(map(float,input().split()))


if lados[0] + lados[1] <= lados[2] or lados[1] + lados[2] <= lados[0] or lados[0] + lados[2] <= lados[1]:
    area = ((lados[0] + lados[1]) * lados[2]) / 2 
    print(f"Area = {area}")
else:
    perimetro = lados[0] + lados[1] + lados[2]
    print(f"Perimetro = {perimetro:.1f}")


