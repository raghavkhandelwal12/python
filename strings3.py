#python modify the string
#python has a set of built in methods that you can use on strings

#the upper method return the string in upper case

# x='hello world'
# print(x.upper())# this method convert the string in the upper case if it is in the lower case

#the lower case method

# x='HELLO WORLD'
# print(x.lower())#it convert the string in the lower case if the strings in the upper case

#remove whitespace
#whitespace is the space before after the actual text and very often you want to remove this space

# a='   hello world  '
# print(a)
# print(a.strip()) #this method remove the space at the starting and the ending of the line


#replace the string
#the replace method() replaces a string with another strings
# a='hello world'
# print(a.replace('hello','wollo'))


#split string
#the split() string method returns a list where the text between the specified separtor the list items

a='hello. world'
print(a.split(","))