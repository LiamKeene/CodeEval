import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # Ignore empty lines
    if not test == '\n':
        # Split the input into the coded string and keys
        string, keys = test.split('|')

        # Keys are 1-based but to access the code change to 0-based
        keys = [int(key) - 1 for key in keys.split()]
        print ''.join(string[key] for key in keys)

test_cases.close()
