import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    # Split sentence into words
    words = test.split()
    # Need to capitalise the first char - using capitalize() will remove all
    # capitals that are not the first char - ie javaScript -> Javascript
    output = []
    for word in words:
        word = ''.join([word[0].upper(), word[1:]])
        output.append(word)
    print ' '.join(output)

test_cases.close()
