#!/usr/bin/env ruby
from=ARGV[0].scan(/\[from:(.*?)\]/).join
to=ARGV[0].scan(/\[to:(.*?)\]/).join
flag=ARGV[0].scan(/\[flags:(.*?)\]/).join
print from
print ","
print to
print ","
print flag
puts ""
