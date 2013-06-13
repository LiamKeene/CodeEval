# Print out the second to last word in a line
File.open(ARGV[0]).each_line do |line|
  puts line.split()[-2]
end
