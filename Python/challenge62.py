import sys

def mod(n, m):
    """Calculate the modulus without using the % operator.

    n / m returns the closest multiple, so if we multiply this by m and subtract
    from n we should have the modulus.

    """
    return n - ((n / m) * m)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    n, m = test.strip().split(',')
    print mod(int(n), int(m))

test_cases.close()
