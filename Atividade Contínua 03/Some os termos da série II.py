numerodefracoes=int(input())
soma=-1
for x in range(2,numerodefracoes+1):
    if x % 2 == 0:
       soma+=1/x
    else:
       soma-=1/x
print("{:.6f}".format(soma))
