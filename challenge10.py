import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    elems = test.split()
    index = int(elems.pop())
    if not index > len(elems):
        print elems[-int(index)]

test_cases.close()
