import sys

def find_multiple(n, p):
    """Finds the first multiple of p that is greater than n."""
    while p < n:
        p += p
    return p

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    n, p = [int(elem) for elem in test.split(',')]
    print find_multiple(n, p)

test_cases.close()
