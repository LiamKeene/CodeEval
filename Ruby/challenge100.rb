# Prints 1 if a number is even and 0 if it is odd
File.open(ARGV[0]).each_line do |line|
  # Love Ruby one liners
  if line.strip().to_i%2 == 0 then puts 1 else puts 0 end
end
