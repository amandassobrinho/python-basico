def formatacao(lista):
    string=""
    for numero in lista:
        string += str(numero) + ' '
    print(string.strip())
lista_numeros = list(map(int, input().split()))
comando=input()
while comando !="final":
    numero=comando.split()
    if numero[0]=="inserir":
        lista_numeros.append(int(numero[1]))
    elif numero[0]=="parcial":
        lista_numeros.sort()
        formatacao (lista_numeros)
    elif numero[0]=="remover":
        lista_numeros.remove(int(numero[1]))
    comando=input()
    
