#!/usr/bin/env ruby
i=ARGV[0]
b=ARGV[0].scan(/[0-9]{10}/).join
if b==i then
    puts b
else
  puts ""
end
