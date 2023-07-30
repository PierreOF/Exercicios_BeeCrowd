Quartos = int(input())
ValoresQuartos=list(map(int,input().split()))

SomaAtual=MaiorSoma=0

for i in ValoresQuartos:
   SomaAtual+=i

   MaiorSoma = max(MaiorSoma,SomaAtual)
   
   if SomaAtual<0:
       SomaAtual=0


print(MaiorSoma)

