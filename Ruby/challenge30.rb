def find_intersection(list1, list2)
  # Returns the points of intersection between two lists
  output = []
  list1.each { |elem| output << elem if list2.include?(elem) }
  return output.join(',')
end

File.open(ARGV[0]).each_line do |line|
  list1, list2 = line.strip.split(';')
  puts find_intersection(list1.split(','), list2.split(','))
end
