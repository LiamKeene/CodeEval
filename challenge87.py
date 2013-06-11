import sys

board_dim = 256
x_range = xrange(board_dim)
y_range = xrange(board_dim)

matrix = [[0 for x in x_range] for y in y_range]

def query_col(i):
    """Return sum of values on column i."""
    print sum([row[i] for row in matrix])

def query_row(i):
    """Return sum of values on row i."""
    print sum(matrix[i])

def set_col(i, value):
    """Set value on all elements in column i."""
    for row in matrix:
        row[i] = value

def set_row(i, value):
    """Set value on all elements in row i."""
    for j in xrange(len(matrix[i])):
        matrix[i][j] = value

def do_action(statement):
    """Determine the action to perform."""
    actions = {
        'QueryCol': query_col,
        'QueryRow': query_row,
        'SetCol': set_col,
        'SetRow': set_row,
    }
    vals = statement.split(' ')
    action = actions.get(vals[0])
    args = [int(val) for val in vals[1:]]
    action(*args)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    do_action(test)

test_cases.close()
