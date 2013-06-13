import sys

def check_bit_positions(n, p1, p2):
    """Checks if the first two digits of n match p1 and p2."""
    li = list(str(n))
    if int(li[0]) == p1 and int(li[1]) == p2:
        return 'true'
    return 'false'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    n, p1, p2 = [int(elem) for elem in test.split(',')]
    print check_bit_positions(n, p1, p2)

test_cases.close()
