n = int(input())
result = 0

for i in range(n):
    q, y = input().split()
    result += (float(q) * float(y))

print(result)
