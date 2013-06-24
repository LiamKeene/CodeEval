def remove_duplicates(s)
  # Remove duplicates from a string
  output = []
  s.strip.split(',').each { |e| output << e if not output.include?(e) }
  return output.join(',')
end

File.open(ARGV[0]).each_line do |line|
  puts remove_duplicates(line)
end
