
for i in range(999,900,-1):
    for j in range(999,900,-1):
        result = str(i * j)
        if result == result[::-1]:
            print(i,j,result)


