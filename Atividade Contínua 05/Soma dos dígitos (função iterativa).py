def somaDigitos(n):
    s = 0
    while n:
        s += n % 10
        n //=10
    return s
n=(int(input()))
print(somaDigitos(n))
