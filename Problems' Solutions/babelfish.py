import sys

dic = {}

for line in sys.stdin:
    if line.strip() == '':
        break
    else:
        m = line.split()
        dic[m[1]] = m[0]

for line in sys.stdin:
    if line.strip() in dic:
        print(dic[line.strip()])
    else:
        print("eh")
