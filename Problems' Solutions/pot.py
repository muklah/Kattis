import math

n = int(input())
x = 0

for i in range(n):
    p = int(input())
    power = p % 10
    num = math.floor(p / 10)
    x += num**power

print(x)