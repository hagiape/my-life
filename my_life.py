# Write a method in python to write multiple line of text 
# contents into a text file mylife.txt. See sample output:
# Enter line: Beautiful is better than ugly.
# Are there more lines y/n? y
# Enter line: Explicit is better than implicit.
# Are there more lines y/n? y
# Enter line: Simple is better than complex.
# Are there more lines y/n? n 

my_life = open('mylife.txt', 'a')
while True:
    new_line = input('Enter line: ')
    my_life.write(new_line + '\n')
    prompt = input('Are there more lines? yes/no: ')
    if prompt == 'no':
        break
    else:
        if prompt != 'yes':
            print('Only answer "yes" or "no". Please try running the program again')
            break
my_life.close()
