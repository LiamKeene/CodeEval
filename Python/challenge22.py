import sys

def get_fibonacci(n):
    """Returns the nth number in the Fibonacci sequence.

    Uses Binet's Fibonacci formula.

    """
    return int(
        (
            (1 + 5**0.5)**n - (1 - 5**0.5)**n
        ) / (2**n * 5**0.5)
    )

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    print get_fibonacci(int(test))

test_cases.close()
