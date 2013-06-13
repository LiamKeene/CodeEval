# Print out the mth to last element
File.open(ARGV[0]).each_line do |line|
  elems = line.split()
  # index of element to print
  index = elems.pop().to_i
  if not index > elems.length
    puts elems[-index]
  end
end
