def is_prime(num):
    num_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            num_divisors += 1
    if num_divisors == 2:
        return True
    else:
        return False

for i in range(1, 20):
    if is_prime(i + 1):
            print(i + 1, end=" ")
print()