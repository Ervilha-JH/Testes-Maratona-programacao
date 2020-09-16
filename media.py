lstN = []
a,b = input().split(" ")
lstN = input().split(" ")
soma = 0
inicio = int(a) - int(b)
for i in range(inicio, len(lstN)):
    soma = soma + int(lstN[i])

media = soma/int(b)
print("%.0f" % media)