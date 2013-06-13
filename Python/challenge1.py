import sys

def play_fizz_buzz(a, b, n):
    """Play Fizz Buzz.

    Args:
        a: the first number to divide by
        b: the second number to divide by
        n: the maximum number to count to

    Returns:
        a string containing the numbers from 1 to n, where a number that is
        divisible by a is replaced by 'F' and where a number that is divisible
        by b is replaced by 'B'.  A number that is divisible by a and b is
        replaced by 'FB'.

    """
    output = []
    for i in xrange(1, n+1):
        # Conditions for Fizz and Buzz
        fizz = (i)%a == 0
        buzz = (i)%b == 0

        # Logic for replacing numbers with 'F', 'B' or 'FB'
        if fizz and buzz:
            output.append('FB')
        elif fizz and not buzz:
            output.append('F')
        elif not fizz and buzz:
            output.append('B')
        else:
            output.append(str(i))

    return ' '.join(output)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if not test == '\n':
        a, b, n = [int(elem) for elem in test.split()]
        print play_fizz_buzz(a, b, n)

test_cases.close()
