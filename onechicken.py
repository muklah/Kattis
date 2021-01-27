import sys

n, m = input().split()

q = 0
p = 0

piece = ""

if(int(n) == int(m) or int(n) > 1000 or int(m) > 1000):
    sys.exit()

if(int(n) < int(m)):
    p = int(m)-int(n)
    piece = "piece" if p == 1 else "pieces"
    print(f"Dr. Chaz will have {p} {piece} of chicken left over!")

else:
    q = int(n)-int(m)
    piece = "piece" if q == 1 else "pieces"
    print(f"Dr. Chaz needs {q} more {piece} of chicken!")