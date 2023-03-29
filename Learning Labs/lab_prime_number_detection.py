def is_prime(num):
    #
    #
    for p in range (2, i):
        if num % p == 0:
            return False
    return True
    
    #

for i in range(1, 38):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
