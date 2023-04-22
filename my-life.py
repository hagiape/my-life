# Write a method in python to write multiple line of text 
# contents into a text file mylife.txt. See sample output:
# Enter line: Beautiful is better than ugly.
# Are there more lines y/n? y
# Enter line: Explicit is better than implicit.
# Are there more lines y/n? y
# Enter line: Simple is better than complex.
# Are there more lines y/n? n 

# read file for appending
my_life = open('mylife.txt', 'a')
# while loop
# input new line
while True:
    new_line = input('Enter line: ')
# write line
# prompt for another line
    my_life.write(new_line + '\n')
    prompt = input('Are there more lines? yes/no: ')
# conditional input
# if no then break, if input is neither yes/no then break