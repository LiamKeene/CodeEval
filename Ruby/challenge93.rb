File.open(ARGV[0]).each_line do |line|
  words = line.split()
  # Capitalise the first char - using string.capitalize will remove all capitals
  # that appear later in the word - ie 'javaScript'.capitalize -> 'Javascript'
  output = []
  words.each { |word| output << [word[0].upcase, word[1..-1]].join }
  puts output.join(' ')
end
