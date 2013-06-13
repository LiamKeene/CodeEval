import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # Use string.swapcase method
    print test.swapcase()

test_cases.close()
