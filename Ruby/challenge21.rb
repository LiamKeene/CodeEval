def sum_integer(n)
  # Split the number into digits and use inject with a `memo`
  return n.split(//).inject(0) { |sum, n| sum + n.to_i }
end

File.open(ARGV[0]).each_line do |line|
  puts sum_integer(line.strip())
end
