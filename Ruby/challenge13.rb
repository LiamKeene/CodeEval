def scrub_string(string, scrub)
  # Removes given characters from a string
  output = []
  string.each_char { |c| output << c if not scrub.include?(c) }
  return output.join
end

File.open(ARGV[0]).each_line do |line|
  string, scrub = line.split(', ')
  puts scrub_string(string, scrub)
end
