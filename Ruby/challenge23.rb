# Maximum size of table
MAX = 12

# Create x and y ranges
x_range = (1..MAX)
y_range = (1..MAX)

# Multiply each x_range element by each y_range element and format
y_range.each do |y|
  x_range.each { |x| print '%4d' % (x * y) }
  puts ''
end
