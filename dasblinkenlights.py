p, q, s = input().split()

pset = set()
qset = set()
a = int(p)
while a <= int(s):
    pset.add(a)
    a += int(p)
a = int(q)
while a <= int(s):
    qset.add(a)
    a += int(q)
ans = (pset & qset)
if len(ans):
    print('yes')
else:
    print('no')
