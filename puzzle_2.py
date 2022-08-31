
fibs = [0,1,1,2]


next_fib = 3
while next_fib < 4000000:
    fibs.append(next_fib)
    next_fib = fibs[len(fibs)-1] + fibs[len(fibs)-2]

print(fibs)

total = 0
for fib in fibs:
    if fib % 2 == 0:
        total += fib

print(total)
