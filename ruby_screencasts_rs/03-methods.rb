#!/usr/bin/env ruby -w
# -*- coding: utf-8 -*-

puts "------------------------------ print_hello ------------------------------"

def print_hello
    puts "Hello World!"
end

print_hello

puts "--------------------------- print_hello_one ---------------------------------"

def print_hello_one(name)
    puts "Hello, " + name + "!"
end

print_hello_one("Elsa")
print_hello_one("Anna")
print_hello_one("Kristoff")
print_hello_one("Olaf")

puts "--------------------------- print_hello_two ---------------------------------"

def print_hello_two(*args)
    args.each { |name|
        if name =~ /---.*/
            puts name
        else
            puts "Hello, " + name + "!"
        end
    }
end

print_hello_two("--------------------", "Elsa")
print_hello_two("--------------------", "Elsa", "Anna")
print_hello_two("--------------------", "Elsa", "Anna", "Kristoff")
print_hello_two("--------------------", "Elsa", "Anna", "Kristoff", "Olaf")

puts "------------------------------------------------------------"

def print_hello_three(one="", two="", tree="", four="")
    # args = method(__method__).parameters.map { |arg| arg[1].to_s }
    args = method(__method__)
        .parameters
        .map { |_, v| [v, binding.local_variable_get(v)] }
        .map { |arg| arg[1].to_s }

    everyone = ""
    args.each { |name|
        unless name.empty?
            # print name
            everyone += name + ", "
        end
    }

    if everyone.empty?
        puts "Nobody is here..."
    else
        puts "Here is: " + everyone.delete_suffix(", ")
    end
end

print_hello_three
print_hello_three("Elsa")
print_hello_three("Elsa", "Anna")
print_hello_three("Elsa", "Anna", "Kristoff")
print_hello_three("Elsa", "Anna", "Kristoff", "Olaf")

puts "-------------------------- get_names_one ----------------------------------"

def get_names_one(one="", two="", tree="", four="")
    # args = method(__method__).parameters.map { |arg| arg[1].to_s }
    args = method(__method__)
        .parameters
        .map { |_, v| [v, binding.local_variable_get(v)] }
        .map { |arg| arg[1].to_s }

    everyone = ""
    args.each { |name|
        unless name.empty?
            # print name
            everyone += name + ", "
        end
    }

    # return everyone
    everyone.delete_suffix(", ")
end

puts get_names_one
puts get_names_one("Elsa")
puts get_names_one("Elsa", "Anna")
puts get_names_one("Elsa", "Anna", "Kristoff")
puts get_names_one("Elsa", "Anna", "Kristoff", "Olaf")

puts "------------------------------------------------------------"
