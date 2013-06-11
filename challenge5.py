import sys

def detect_cycle(num_list):
    """Find cycle using Floyd's algorithm."""
    turtle, hare = 1, 2
    # Find when x_i = x_2i by skipping ahead by 2
    while num_list[turtle] != num_list[hare]:
        turtle += 1
        hare += 2

        # If the hare has past the length of the list, return None
        if hare >= len(num_list):
            return None, None

    # Find the start of the cycle
    mu = 0
    # Start turtle from 0, but start hare from position turtle finished at when
    # the cycle was found
    turtle, hare = 0, turtle
    while num_list[turtle] != num_list[hare]:
        turtle += 1
        hare += 1
        mu += 1

    # Finally find the length of the cycle
    lam = 1
    # Turtle does not move but hare moves by one.
    hare = turtle + 1
    while num_list[turtle] != num_list[hare]:
        hare += 1
        lam += 1

    return mu, lam

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    nums = test.strip().split(' ')

    # Only process lines with a sequence
    if not nums == '':
        mu, lam = detect_cycle(nums)
        # Ignore failed sequences
        if not mu:
            continue
        print ' '.join(nums[mu:mu+lam])

test_cases.close()
