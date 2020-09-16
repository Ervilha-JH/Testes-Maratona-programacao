a,b = input().split(" ")
resul = float(b) / float(a)
resulb = (resul - 1) * 100
if(resulb > 15):
    print('ALTA')
elif(resulb < - 15):
    print('QUEDA')
elif(resulb >= -15 or resulb <= 15):
    print('ESTAVEL')