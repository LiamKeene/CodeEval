# Swap the case of the text in each line
File.open(ARGV[0]).each_line do |line|
    puts line.swapcase
end
