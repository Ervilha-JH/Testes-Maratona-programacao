a,b = input().split(" ")
for i in range(0,int(b)):
    letra,regra = input().split(" ")
    a = a.replace(letra,regra)
print(a)