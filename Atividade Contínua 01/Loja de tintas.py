import math

#constantes
metrosPintados_24 = 24 * 7
metrosPintados_5= 5.4 * 7
preco_24=91.0
preco_5=23.0

entrada=float(input())
#somente latas de 24
quantidadeLatas_so24 = math.ceil(entrada/metrosPintados_24)
print("a)",quantidadeLatas_so24, "lata(s) de 24 litros: R$",
"{:,.2f}".format(preco_24 * quantidadeLatas_so24))
#somente latas de 5.4
quantidadeLatas_so5 = math.ceil(entrada/metrosPintados_5)
print("b)",quantidadeLatas_so5, "lata(s) de 5.4 litros: R$",
"{:,.2f}".format(preco_5 * quantidadeLatas_so5))
#ambas as latas
metrosQueFaltaram = entrada % metrosPintados_24
latasdetintasqueprecisamserusadas_5=math.ceil(metrosQueFaltaram / metrosPintados_5)

dinheirogasto_5=latasdetintasqueprecisamserusadas_5 * preco_5
latasdetintasqueprecisamserusadas_24= (entrada-metrosQueFaltaram) /metrosPintados_24
dinheirogasto_24=latasdetintasqueprecisamserusadas_24 * preco_24
print("c)",int(latasdetintasqueprecisamserusadas_24),"lata(s) de 24 litros e",
latasdetintasqueprecisamserusadas_5,"lata(s) de 5.4 litros: R$",
"{:,.2f}".format(dinheirogasto_5+dinheirogasto_24))
