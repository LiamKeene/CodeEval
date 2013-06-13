# Print the position of the right most occurence of a given character
File.open(ARGV[0]).each_line do |line|
    s, c = line.strip().split(',')
    # Print rightmost index or -1
    puts s.rindex(c) || -1
end
