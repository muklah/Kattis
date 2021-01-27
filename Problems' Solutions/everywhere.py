t = int(input())

f_result = {}

for i in range(t):
    n = int(input())
    result = []

    for j in range(n):
        c = input()
        result.append(c)

    f_result[i] = [set(result)]
    ee = type(f_result[0])
    print(ee)
