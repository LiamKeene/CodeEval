import operator
import sys

test_cases = open(sys.argv[1], 'r')

# Strip whitespace and remove empty lines
lines = [test.strip() for test in test_cases if not test == '\n']

# Get number of lines to output
num = int(lines.pop(0))

# Map line length with actual line
mapping = dict(zip([len(line) for line in lines], lines))

# Sort mapping based on line length
sorted_lines = sorted(mapping.iteritems(), key=operator.itemgetter(0), reverse=True)

# Print first `num` lines
print '\n'.join([line for length, line in sorted_lines[:num]])

test_cases.close()
