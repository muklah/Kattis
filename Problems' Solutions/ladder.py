import math

h, v = input().split()

x = int(h) / math.sin(math.radians(int(v)))

print(math.ceil(x))
