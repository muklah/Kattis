num1, avg = input().split()

if int(num1) < 1000 and int(avg) < 1000:
    num2 = int(avg)*2 - int(num1)
    print(num2)

else:
    print("numbers must be less than 1000")