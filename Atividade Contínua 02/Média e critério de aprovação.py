p1=float(input())
p2=float(input())
p3=float(input())
fq=float(input())
mediaprovas=round((p1*2+p2*2+p3*3)/7,1)
print("Frequencia: {:.0f}%".format(fq*100))
print("Media: {:.1f}".format(mediaprovas))
if (fq<0.75):
    print ('Aluno reprovado por faltas!')
elif (mediaprovas>9):
    print ('Aluno aprovado com louvor!')
elif (mediaprovas>=6):
    print ('Aluno aprovado!')
elif(mediaprovas>=4):
    print ('Aluno de recuperaçao!')
else:
    print('Aluno reprovado!')
