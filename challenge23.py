# Maximum size of table
MAX = 12

# Create x and y ranges
x_range = xrange(1, MAX+1)
y_range = xrange(1, MAX+1)

# Multiply each x_range element by each y_range element and format
for y_index in y_range:
    print ''.join(['{:>4}'.format(y_index * x_index) for x_index in x_range])
