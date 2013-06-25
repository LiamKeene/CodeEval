def is_pangram(line)
  # Returns letter missing from line to create a pangram or NULL if it is one
  req_letters = (97..122).map(&:chr)

  line.downcase.each_char { |c|
    if c.ord >= 97 && c.ord <= 122
      if req_letters.include?(c)
        req_letters.delete(c)
      end
    end
  }
  return req_letters == [] ? 'NULL' : req_letters.join
end

File.open(ARGV[0]).each_line do |line|
  puts is_pangram(line.strip)
end
