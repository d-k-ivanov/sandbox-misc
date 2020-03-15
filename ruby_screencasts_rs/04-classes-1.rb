#!/usr/bin/env ruby -w
# -*- coding: utf-8 -*-

class Item

    def initialize
        @price = 30
        @weight = 1000
    end

    def price
        @price
    end

    def price=(price_value)
        @price = price_value
    end

    def weight
        @weight
    end

    def weight=(weight_value)
        @weight = weight_value
    end


end

puts "------------------------------------------------------------"
item1 = Item.new
item2 = Item.new
item3 = Item.new

puts item1.price
puts item2.price
puts item3.price

puts item1.weight
puts item2.weight
puts item3.weight

puts "------------------------------------------------------------"

p item1
p item2
p item3

puts "------------------------------------------------------------"

item1.price=(rand(100))
item2.price=(rand(100))
item3.price=(rand(100))

puts item1.price
puts item2.price
puts item3.price

puts "------------------------------------------------------------"

item1.price = rand(100)
item2.price = rand(100)
item3.price = rand(100)

puts item1.price
puts item2.price
puts item3.price

puts "------------------------------------------------------------"
