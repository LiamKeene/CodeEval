import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    li = [float(elem) for elem in test.split()]
    li.sort()
    print ' '.join(['{:.3f}'.format(elem) for elem in li])

test_cases.close()
