#a regex or regular expression is a sequence of character that forms  a search pattern
#regex can be used to check if a string contains the specified search pattern

#regex has a built in package called re which cna be used to work with regular expression
#search the string to see if it starts with The and ends with spain

# import re
# txt="the rain in spain"
# x=re.search("^the.*spain$",txt)
# if x:
#     print('yes!we have a match')
# else:
#     print('no match')


#the findall() function returns a list containing all matches

# import re
# txt='the rain in spain'
# x=re.findall('ai',txt)
# print(x)


#the list contains the matches in the order they are found
#if not matches are found an empty list is returned

# import re
# txt='the rain in spain'
# x=re.findall('raghav',txt) #if the pattern is not found it give the error
# print(x)


#the search function
#the search function searches the strings for a match and return the mathc objects if there is match

import re
txt='the rain in spain'
x=re.search('\s',txt)
print('the first white-space character is located in position:',x.start())