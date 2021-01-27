n = int(input())
result = []

for i in range(n):
    x = int(input())
    result.append(x)

for x in result:
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
