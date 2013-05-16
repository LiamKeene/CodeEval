import sys

def find_intersection(list1, list2):
    """Returns the intersection of the two given lists.

    Lists are comma separated strings.
    """
    list1 = list1.split(',')
    list2 = list2.split(',')
    output = []
    for elem in list1:
        if elem in list2:
            output.append(elem)

    return ','.join(output)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    list1, list2 = test.strip().split(';')

    print find_intersection(list1, list2)

test_cases.close()
