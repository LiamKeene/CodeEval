import re
import sys

points_re = re.compile(r'''
    \(
    (-?\d{1,3})
    \,\s
    (-?\d{1,3})
    \)\s\(
    (-?\d{1,3})
    \,\s
    (-?\d{1,3})
    \)
''', re.VERBOSE)

def calculate_distance(p1, p2):
    """Calculate distance between two (x, y) points.

    Uses Pythagoras' theorem.
    """
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # Match
    points = points_re.match(test.strip())
    x1, y1, x2, y2 = [int(point) for point in points.groups()]
    dist = calculate_distance([x1, y1], [x2, y2])
    print '{:.0f}'.format(dist)

test_cases.close()
