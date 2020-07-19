x=int(input())
n=int(input())
multiplosEncontrados=0
for contador in range(1,n):
    if contador*x < n:
        multiplosEncontrados = multiplosEncontrados + 1
    else:
        break
print("O numero", x, "tem", multiplosEncontrados, "multiplos menores que", str(n) + ".")
