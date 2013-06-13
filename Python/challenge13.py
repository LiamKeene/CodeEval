import sys

def scrub_string(string, scrub):
    """Removes given characters from a string."""
    out = []
    for char in string:
        if not char in scrub:
            out.append(char)
    return ''.join(out)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    string, scrub = test.split(', ')
    print scrub_string(string, scrub)

test_cases.close()
