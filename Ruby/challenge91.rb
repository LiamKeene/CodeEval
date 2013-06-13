# Sort the numbers in a line
File.open(ARGV[0]).each_line do |line|
  # Create a list from each line
  li = []
  line.split(' ').each { |n| li.push(n.to_f) }
  # Sort the list
  li.sort!
  # For each element format to 3 decimal places
  li.each_index { |i| li[i] = '%.3f' % li[i]}
  # Join list
  puts li.join(' ')
end
