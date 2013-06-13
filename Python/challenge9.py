import sys

class LIFOStack(object):
    """Simple LIFO (last in first out) stack."""
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def pop_n(self, n):
        """Pop and print out every nth element in stack."""
        for i in xrange(0, len(stack)):
            if i % n == 0:
                yield self.pop()
            else:
                self.pop()


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    stack = LIFOStack()

    # 'push' each value to the stack
    [stack.push(num) for num in test.strip().split(' ')]

    # Pop and print out each alternate element
    print ' '.join(list(stack.pop_n(2)))

test_cases.close()
