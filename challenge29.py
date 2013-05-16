import sys

def remove_duplicates(s):
    """Returns a string s with duplicated elements removed."""
    output = []
    for elem in s.strip().split(','):
        if elem not in output:
            output.append(elem)

    return ','.join(output)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    print remove_duplicates(test)

test_cases.close()
