l = int(input())
d = int(input())
x = int(input())

result = []

for i in range(l, d+1):
    t = str(i)
    sum = 0

    for j in t:
        sum += int(j)

    if(sum == x):
        result.append(t)
        
print(result[0])
print(result[-1])
