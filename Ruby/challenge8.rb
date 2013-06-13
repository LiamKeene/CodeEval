# Reverse the words in a sentence
File.open(ARGV[0]).each_line do |line|
  words = line.split()
  puts words.reverse.join(' ')
end
