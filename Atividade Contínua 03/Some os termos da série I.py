numerodefracoes=int(input())
soma=0
for x in range(1,numerodefracoes+1):
    soma+=1/x**2
print("{:.6f}".format(soma))
