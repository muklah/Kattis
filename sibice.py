import math

matches, width, height = input().split()
matches_list = []

dimeter = int(math.sqrt(int(width)**2 + int(height)**2))

for match in range(int(matches)):
    match = int(input())
    matches_list.append(match)

for match in matches_list:
    if match <= dimeter:
        print("DA")
    else:
        print("NE")
