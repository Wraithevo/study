numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for n in numbers:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            not_primes.append(n)
            break
    if is_prime == True and n != 1:
        primes.append(n)
print("Primes: ", primes)
print("Not primes: ", not_primes)