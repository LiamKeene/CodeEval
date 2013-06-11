import sys

def is_pangram(line):
    """Returns the required letters to create a pangram or NULL if it is one."""
    req_letters = [chr(i) for i in xrange(97, 123)]

    letters = list(line.strip().lower())
    for letter in letters:
        # Ensure the letter is in a-z set
        if ord(letter) >= 97 and ord(letter) <= 122:
            # Remove it from required letters
            if letter in req_letters:
                req_letters.remove(letter)

    if req_letters == []:
        return 'NULL'
    return ''.join(req_letters)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    print is_pangram(test)

test_cases.close()
