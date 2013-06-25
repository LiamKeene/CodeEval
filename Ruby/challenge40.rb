def self_describing(n)
  # Returns true if a number is self-describing
  digits = n.to_s.split(//).map(&:to_i)

  # Return 1 if the ith digit equals the count of that digit
  digits.each_index { |i| return (digits[i] == digits.count(i)) ? 1 : 0 }

end

File.open(ARGV[0]).each_line do |line|
  puts self_describing(line.strip)
end
