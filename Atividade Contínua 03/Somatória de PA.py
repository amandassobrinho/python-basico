razao=int(input())
limite=int(input())
soma=0
for c in range(1,limite+razao,razao):
    soma+=c
print("A somatoria da PA eh: {}".format(soma))
