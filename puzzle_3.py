from math import sqrt

test = 600851475143

def test_for_prime(value):
    factor = test / value
    is_prime = True
    for i in range(2, int(sqrt(factor))):
        if factor % i == 0:
            is_prime = False
    return is_prime


found = False
factor = 2
while not found:
    if test % factor == 0:
        #print(factor)
        found = test_for_prime(factor)
        if found:
            print('Factor:' , factor)
    factor += 1

factor -= 1
print(factor)
print(test / factor)
