import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    string, letter = test.strip().split(',')
    print string.rfind(letter)

test_cases.close()
