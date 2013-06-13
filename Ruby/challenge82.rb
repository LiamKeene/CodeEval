File.open(ARGV[0]).each_line do |line|
  digits = line.strip().split(//)
  # Determine if number is an Armstrong number
  sum = digits.inject(0) { |sum, n| sum + n.to_i ** digits.length }
  # Print 'True' or 'False' based on result
  if sum == line.to_i then puts 'True' else puts 'False' end
end
