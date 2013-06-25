def is_happy(num)
  # Determines if a given number is happy
  seen = []

  # Loop until num is 1 or already seen
  until num == 1 || seen.include?(num)
    seen << num
    # Crazy one liner - convert num to string, convert characters to integers
    # and square then sum the resulting array
    num = num.to_s.chars.map{ |digit| digit.to_i ** 2}.inject(:+)
  end

  return num == 1 ? 1 : 0
end

File.open(ARGV[0]).each_line do |line|
  puts is_happy(line.strip.to_i)
end
