def is_prime(n)
  # Use divisor test to determine if number is prime
  (3..n**0.5+1).step(2) { |x| return false if n % x == 0 }
  # No divisors found, thus number is prime
  return true
end

# Number of primes
max_n = 1000

# Output of primes (start with 2)
output = [2, ]

# First prime to check is 3
i = 3

until output.length == max_n
  # Add to output if prime
  output << i if is_prime(i)
  # Skip even numbers obviously
  i += 2
end

# Sum the primes
puts output.inject(:+)
