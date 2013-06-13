import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # Remove new line characters
    test = test.strip('\n')

    # Convert to list of integers
    nums = [int(num) for num in test]

    # Determine if number is an Armstring number
    print int(test) == sum([num ** len(nums) for num in nums])

test_cases.close()
