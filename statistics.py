import sys

count = 1

for line in sys.stdin.readlines():
    t = map(int, line.split())
    print(t)
    n = t[0]
    l = t[1:n+1]
    l_min = min(l)
    l_max = max(l)
    rang = l_max - l_min
    print(f"Case {count}: {l_min} {l_max} {rang}")
    count +=1
