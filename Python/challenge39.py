import sys

def is_happy(num):
    """Determines if given number is happy.

    Replace number by sum of squares of the digits in the number until we get to
    1.  Returns 1 (True) if this can be achieved.

    Returns 0 (False) if during check the same number if encountered.

    """
    seen = []
    while not num == 1 and num not in seen:
        #
        seen.append(int(num))
        num = sum([int(digit) ** 2 for digit in str(num)])
    return 1 if num == 1 else 0

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip('\n')
    print is_happy(test)

test_cases.close()
