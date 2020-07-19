salario=float(input())

if(salario<=1751.81):
    print("Desconto do INSS: R$ {:.2f}".format (salario * 8/100))
elif(salario>= 1751.82 and salario <=2919.72):
    print( "Desconto do INSS: R$ {:.2f}".format (salario * 9/100 ))
elif(salario>= 291.73 and salario <=5839.45):
    print( "Desconto do INSS: R$ {:.2f}".format (salario * 11/100 ))
elif(salario> 5839.45):
    print("Desconto do INSS: R$ {:.2f}".format (5839.45 *11/100))
