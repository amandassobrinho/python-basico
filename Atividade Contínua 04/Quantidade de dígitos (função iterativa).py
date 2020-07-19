n=input()

def contar_numeros(n):
    digitos=0
    for x in n:
        digitos+=1
    return digitos

print(contar_numeros(n))
