import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # Print 1 if even (modulus 2 is zero) or else 0
    print 1 if int(test)%2 == 0 else 0

test_cases.close()
