while True:
    try:
        n = int(input())
    except ValueError:
        continue
    if n == 0:
        break

    s = str(n)
    n_sum = 0

    for i in s:
        n_sum += int(i)

    for p in range(11, 100000):
        p_sum = 0
        mult = n * p
        str_p = str(mult)
    
        for j in str_p:
            p_sum += int(j)
        if(p_sum == n_sum):
            print(p)
            break
