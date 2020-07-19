import math

a = float(input())
b = float(input())
c = float(input())
d = float(input())

# precedencia de processamento matematico:
# potencia **
# divisao e multiplicaçao / *
# soma e subtraçao + -

print("i)", round((a * a + 3 * b )/ c + d, 4))

print("ii)", round(math.log(a, 10) + math.exp(-b / c) - (d * d) / math.pi, 4))

print("iii)", round(((a * a) ** (1/3) * b ** (1/3) + c * d ) / (a + b + c + d), 4))

print("iv)", round((a + b)*( c + d ) / (a * b * c * d), 4))

print("v)", round(((a * a + b * b) / (c * d))  - (c * c + d * d )/ (a * b), 4))

print("vi)", round(( a + b + c + d) **(2), 4))
