
valores = list(map(float,input().split()))
valores.sort(reverse=True)

a , b , c = valores

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if (a * a) > (b * b) + (c * c):
        print("TRIANGULO OBTUSANGULO")
    if (a * a) < (b * b) + (c * c):
        print("TRIANGULO ACUTANGULO")
    if (a * a) == (b * b) + (c * c):
        print("TRIANGULO RETANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    elif (b==c) or (b==a) or (a==c):
        print("TRIANGULO ISOSCELES")


