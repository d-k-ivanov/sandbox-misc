#!/usr/bin/env ruby -w
# -*- coding: utf-8 -*-
puts "------------------------------------------------------------"

for arg in ARGV
    puts arg
end

puts "------------------------------------------------------------"

for i in 0 ... ARGV.length
    puts "Argumnet \##{i} --> #{ARGV[i]}"
end

puts "------------------------------------------------------------"
a = if ARGV[0]
    b = ARGV[0].to_i
    rand(ARGV[0].to_i)
else
    b = 10
    1
end

while a < b
    puts "'a' var ia " + a.to_s
    a += 1
    sleep 0.1
end

puts "------------------------------------------------------------"
