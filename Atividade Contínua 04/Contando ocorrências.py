caracteres1=input()
caractere2=input()
contador=0
for a in caracteres1:
    if a == caractere2:
        contador=contador+1
if contador>0:
    print("O caractere buscado ocorre {} vezes na sequencia.".format(contador))
else:
    print("Caractere nao encontrado.")
