File.open(ARGV[0]).each_line do |line|
  if not line.strip == ''
    string, keys = line.strip.split('| ')

    # Convert keys to 0-based integers and decode the string
    output = []
    keys.split(' ').each { |key| output << string[key.to_i - 1] }
    puts output.join
  end
end
