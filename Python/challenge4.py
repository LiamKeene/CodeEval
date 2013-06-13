import sys

def is_prime(n):
    """Use divisor test to determine if given number is prime.

    Create a range of odd numbers from 3 until the square root of n (no
    point going past.)

    """
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False

    return True

def sum_primes(max_n):
    """Returns the sum of the first max_n prime numbers.

    """
    # Output list - already includes 2
    output = [2, ]

    # Start testing numbers from 3
    i = 3

    # Create a range using a generator - from max_n down to 3
    while len(output) < max_n:
        # If this number is prime add to output
        if is_prime(i):
            output.append(i)
        i += 2

    return sum(output)

print sum_primes(1000)
