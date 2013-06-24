def fibonacci(n)
  # Returns the nth number of the Fibonacci sequence using Binet's formula.
  return (((1 + 5**0.5)**n - (1 - 5**0.5)**n) / (2**n * 5**0.5)).to_i
end

File.open(ARGV[0]).each_line do |line|
  puts fibonacci(line.to_i)
end
