
test_value = 20
success = False
while not success:
    #print(test_value)
    success = True
    for i in range(1,21):
        if test_value % i != 0:
            success = False
    test_value += 20
print(test_value)
