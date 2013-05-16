import sys

def reverse_words(sentence):
    """Reverse the words in a sentence."""
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    print reverse_words(test)

test_cases.close()
