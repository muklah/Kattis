books = int(input())

prices = [int(input()) for _ in range(books)]

prices.sort()
total = 0
group = []

for price in range(books):
    group.append(prices.pop())
    if len(group) == 3:
        total += sum(group) - min(group)
        group = []

total += sum(group)
print(total)
