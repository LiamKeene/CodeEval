def mod(n, m)
  # Calculates the modulus without using the % operator
  return n - ((n / m) * m)
end

File.open(ARGV[0]).each_line do |line|
  n, m = line.strip().split(',')
  puts mod(n.to_i, m.to_i)
end
