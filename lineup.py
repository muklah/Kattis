import sys

n = int(input())
result = []

for i in range(n):

    m = input()
    if(len(m) < 2 or len(m) > 12):
        break
    for j in m:
        if(j.islower()):
            sys.exit()

    result.append(m)
if(sorted(result) == result):
    print("INCREASING")
elif(sorted(result, reverse=True) == result):
    print("DECREASING")
else:
    print("NEITHER")