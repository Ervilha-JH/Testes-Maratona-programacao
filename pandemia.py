def infectado(l, c, lst, infectacao, count, totalL, totalC):
    if int(infectacao) > int(lst[l][c]):
        lst[l][c] = -1
        if l >= 0  and l < int(totalL) and c >= 0 and c < int(totalC):
            if l + 1 < int(totalL):
                if int(infectacao) > int(lst[l+1][c]) and int(lst[l+1][c]) != -1:
                    count  =+ infectado(l + 1,c, lst, infectacao,count, totalL, totalC)
            if  l - 1 >= 0:
                if int(infectacao) > int(lst[l-1][c]) and int(lst[l-1][c]) != -1:
                    count =+ infectado(l-1,c, lst, infectacao,count, totalL, totalC)
            if  c + 1 < int(totalC):
                if int(infectacao)  > int(lst[l][c+1]) and int(lst[l][c+1]) != -1:
                    count  =+ infectado(l,c + 1, lst, infectacao,count, totalL, totalC)
            if  c - 1 >= 0 :
               if int(infectacao)  > int(lst[l][c-1]) and int(lst[l][c-1]) != -1:
                    count =+ infectado(l,c - 1, lst, infectacao,count, totalL, totalC)
        count = count + 1
    return count

lst1 = []
lst2 = []
a,b = input().split(" ")
for i in range (0,int(a)):
    lst2 = input().split(" ")
    lst1.append(lst2)

l,c,infec = input().split(" ")
count = 0
count = infectado(int(l), int(c), lst1, infec, count, a, b)
print(count)