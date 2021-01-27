megas = int(input())

months = int(input())

result = []
for month in range(months):
    mega = int(input())
    result.append(megas - mega)

print(sum(result) + megas)

# megas_list = [megas - int(input()) for month in range(months)]
# print(sum(megas_list)+10)