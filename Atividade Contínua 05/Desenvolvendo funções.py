from datetime import date
def contaDigitos(numero):
    return len(str(numero))
def ehBissexto(ano): 
    return (ano%4==0 and ano%100!=0) or (ano%400==0)
def Mensagem(menor, ano):
    if menor:
        print("O ano {} foi bissexto".format(ano))
    else:
        print("O ano {} serah bissexto".format(ano))

anos = list(map(int, input().split()))
anoHoje = date.today().year
for ano in anos:
    if contaDigitos(ano) == 4:
        if ehBissexto(ano):
            Mensagem(ano < anoHoje, ano)
        else:
            print("O ano {} NAO eh bissexto".format(ano))
    else:
        print("Ano invalido")
