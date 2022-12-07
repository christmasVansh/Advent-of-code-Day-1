with open('input.txt', 'r') as calorie:
    lines = calorie.readlines()
    calories = [entry.strip() for entry in lines]

sums = []
current_sum = 0
for entry in calories:
    if entry != '':
        current_sum += int(entry)
    elif entry == '':
        sums.append(current_sum)
        current_sum = 0
sums.append(current_sum)

print(max(sums))

#My answer was 69693
