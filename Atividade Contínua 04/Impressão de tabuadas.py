numeroinicial=int(input())
while numeroinicial<1 or numeroinicial>9:
    print("Insira um numero inicial entre 1 e 9")
    numeroinicial=int(input())
numerofinal=int(input())
while numerofinal<1 or numerofinal>9:
    print("Insira um numero final entre 1 e 9")
    numerofinal=int(input())
if numeroinicial>numerofinal:
    print("Nenhuma tabuada nesse intervalo")
for tabuada in range(numeroinicial,numerofinal+1):
    for x in range(1,10):
        print(tabuada,"x",x,"=",tabuada*x)
    print()
