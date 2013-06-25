def longest_lines(num, lines)
  # Sort the lines by length and slice off the first num lines
  lines = lines.sort_by { |line| line.length }
  lines.reverse.slice(0, num)
end

File.open(ARGV[0]) do |f|
  num = f.readline.to_i
  lines = f.readlines.select { |line| line unless line.chomp.empty? }
  puts longest_lines(num, lines)
end
