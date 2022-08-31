
arr = []

for i in range(1000):
    if i % 3 == 0:
        arr.append(i)

for i in range(1000):
    if i % 5 == 0 and i not in arr:
        arr.append(i)

total = 0
for number in arr:
    total += number

print(total)
