import sys

def sum_integer(n):
    """Returns the sum of the digits in an integer."""
    return sum([int(elem) for elem in str(n)])

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    print sum_integer(test.strip())

test_cases.close()
