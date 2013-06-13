File.open(ARGV[0]).each_line do |line|
  n, p = line.split(',').map(&:to_i)
  mult = p
  # Add to mult until it is larger than n
  while mult < n do
    mult += p
  end
  puts mult
end
