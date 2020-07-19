lista_numeros = list(map(int, input().split()))
n = lista_numeros[0]
k = lista_numeros[1]
lista_nome=[]
for a in range (1,n + 1):
    nome=input()
    lista_nome.append(nome)
lista_nome.sort()
print(lista_nome[k-1])
