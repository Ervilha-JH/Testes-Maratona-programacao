a,b = input().split(" ")
resul = int(a) - int(b)
resul = resul / int(b)
if(resul * 100 > 15):
    print('QUEDA')
elif(resul * 100 <= 15 and resul * 100 >= -15):
    print('ESTAVEL')
elif(resul * 100 < -15):
    print('ALTA')