import sys

def is_palindrome(s):
    """Checks if a string is a palindrome."""
    fwd_list = list(s)
    rev_list = list(s)
    # Reverse the string
    rev_list.reverse()

    if fwd_list == rev_list:
        return True

    return False

def is_prime(n):
    """Use divisor test to determine if given number is prime.

    Create a range of odd numbers from 3 until the square root of n (no
    point going past.)

    """
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False

    return True

def find_largest_prime(max_n):
    """Returns the largest prime number given a maxmimum number max_n.

    Because we want the largest prime we will search backwards from max_n.

    """
    # If the maximum number is even (not prime) subtract 1
    if max_n % 2 == 0:
        max_n = max_n - 1

    # Create a range using a generator - from max_n down to 3
    for i in xrange(max_n, 2, -2):
        # If this number is prime and a palindrome, then print it and quit
        if is_prime(i) and is_palindrome(str(i)):
            print i
            sys.exit(0)

find_largest_prime(1000)
