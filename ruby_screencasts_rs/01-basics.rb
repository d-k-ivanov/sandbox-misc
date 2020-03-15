#!/usr/bin/env ruby -w
# -*- coding: utf-8 -*-

puts "------------------------------------------------------------"

puts "Hello World!"

puts "------------------------------------------------------------"

puts "This is s string"
puts 1
puts 2

puts "3"
puts "4"

puts 5 + 6
puts "7" + "8"

puts "------------------------------------------------------------"

name = "Olaf"
puts "Hello, my name is " + name

puts "------------------------------------------------------------"

puts "Kristoff"
puts 1 + 2
puts 2 * 3
puts 10 / 2
puts 2 - 1

puts 1 == 2
puts 2 == 2
puts 1 < 2

puts "------------------------------------------------------------"

puts (2+3)*5

puts true  && true
puts true  && false
puts false && true
puts false && false
puts true  || true
puts true  || false
puts false || true
puts false || false

puts "------------------------------------------------------------"

a = 10
if a > 1
    puts "In the IF-1 section"
end

elsa_name = "Elsa"
anna_name = "Anna"
if elsa_name == "Elsa" || anna_name == "Anna"
    puts "Hello, my name is Kristoff"
end

unless elsa_name != "Elsa" || anna_name != "Anna"
    puts "Hello, my name is " + elsa_name
    puts "Hello, my name is " + anna_name
end

puts "------------------------------------------------------------"

a = 0
if a > 1
    puts "Number is greater than 1"
end

if a < 1
    puts "Number is less than 1"
end

if a > 1
    puts "Number is greater than 1"
elsif a < 1
    puts "Number is less than 1"
end

a = 1
if a > 1
    puts "Number is greater or than 1"
elsif a < 1
    puts "Number is less or than 1"
else
    puts "Number is equal 1"
end

if a >= 1
    puts "Number is greater or equal than 1"
end

if a <= 1
    puts "Number is less or equal than 1"
end


puts "------------------------------------------------------------"

a = 1
b = rand(20)
while a < b
    puts "'a' var ia " + a.to_s
    a += 1
    sleep 0.1
end

puts "------------------------------------------------------------"
