import sys

def is_self_describing(n):
    """Returns 1 if a number n is self describing or 0 if it is not."""
    digits = [int(digit) for digit in n]

    for i in xrange(len(digits)):
        # If the count of a digit does not equal the digit in that position
        # this number is not self-describing
        if not digits.count(i) == digits[i]:
            return 0
    return 1

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    print is_self_describing(test.strip())

test_cases.close()
