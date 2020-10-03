def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # now n is odd
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i

        # increase by 2, no need to check if divisbile by even numbers
        i += 2

    if n > 2:
        factors.append(n)

    return factors
