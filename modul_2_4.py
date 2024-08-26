numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
a = 0
for number in range(2, len(numbers) + 1):
    is_prime = True
    for j in range(2, number):
        if number % j == 0:
            a = a + 1
    if a == 0:
        primes.append(number)
    else:
        a = 0
        not_primes.append(number)
        is_prime = False
print("primes: ", primes)
print("not_primes: ", not_primes)