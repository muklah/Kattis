import math

n = int(input())

result = []

for i in range(n):
    f = int(input())
    
    result.append(math.factorial(f))

for j in result:
    print(j%10)
