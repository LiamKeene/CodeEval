import operator
import re
import sys

chars_re = re.compile(r'[^a-z]')

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # The description for this challenge is poorly worded!
    # Perhaps that's part of the challenge!
    line = test.lower()

    # Remove characters outside a-z
    line = re.sub(chars_re, '', line)

    # Create a mapping between unique letters and their number of occurences
    mapping = {}
    for letter in line:
        if not letter in mapping.keys():
            mapping[letter] = line.count(letter)

    # Sort the mapping by the occurence count - creates a sorted list in order
    # of the letter occurences
    occurence_list = sorted(mapping.iteritems(), key=operator.itemgetter(1), reverse=True)

    # Calculate the beauty for each letter
    beauty = 0
    weight = 26
    for letter, count in occurence_list:
        beauty += count * weight
        weight -= 1

    print beauty

test_cases.close()
