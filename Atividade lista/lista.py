n=int(input("Quantos nomes deseja digitar:"))
while  n<3 or n>10:
    n=int(input("digite um numero entre 3 e 10:"))
lista_nomes=[]
for a in range (1,n):
    nome=input("digite o {} nome:".format(a,n))
    lista_nomes.append(nome)
print("nomes digitados pelo usuario: " , lista_nomes)
lista_nomes.insert(3,"Teste")
print("lista depois de inserir teste na posição 3:",lista_nomes)
del lista_nomes[2]
print("lista depois de excluir indice na posição 2:",lista_nomes)
Ana=lista_nomes.count("Ana")
if Ana>0:
    msg = "O nome Ana apareceu {} vez(es) na lista. Primeira ocorrência - índice: {}"
    msg = msg.format(Ana, lista_nomes.index("Ana"))
    print(msg)
else:
    print("o nome Ana não existe na lista")
lista_nomes.sort()
print("lista ordenada:" ,lista_nomes)
