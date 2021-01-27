n = int(input())
result = []

for i in range(n):
    r, e, c = input().split()

    rf = int(r)
    ef = int(e)
    cf = int(c)
    
    if(ef - rf > cf):
        result.append("advertise")

    elif(ef - rf == cf):
        result.append("does not matter")

    elif(ef - rf < cf):
        result.append("do not advertise")

for output in result:
    print(output)