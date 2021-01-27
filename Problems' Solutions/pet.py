result = 0
a = []
for i in range(5):
    g1, g2, g3, g4 = input().split()
    result = int(g1) + int(g2) + int(g3) + int(g4)
    a.append(result)
print(a.index(max(a))+1, max(a))