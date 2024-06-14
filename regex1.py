#a regex or regular expression is a sequence of character that forms a search pattern
#regex can be used to check if a string contains the specified search pattern

#regex module
#python has a built in package called re which can be used to work with regular expression

#import the re module
# import re
# txt='the rain in spain'
# x=re.search("^the.*spain$",txt)

# if x:
#     print('yea!we have a match')
# else:
#     print("no match")

#regex function
#the re module offers a set of functions that allows us to search string for a match


#the findall() function return a list containing all matches
#print a list of all matches
# import re
# txt="The rain in Spain"
# x=re.findall('i',txt) #this give the how many time the word appear in the text and give the form of the list
# print(x)

#the list contains the matches in the order they are found
#If no matches are found an empty list is returned

# import re
# txt="The rain in spain"
# x=re.findall('raghav',txt) #it give the empty list if the any word not present
# print(x)


#the search function
#the search function searches the string for a match and return  a match object if there is match
#if there is more than one match only the first occurence of the match will be returned

# import re
# txt="theert rain in Spain" 
# x=re.search(r'\s',txt) #this tell the first space which position
# print("the first white space characted is located in position:",x.start())


#if not mathces are found the value none is returned
# import re
# txt='The rain in Spain'
# x=re.search('raghav',txt) #if there is no word which is match the patterin it gives the erro
# print(x)


#the split() function
#the split function returns a list where the string has been split at each match

#split at each white space chareacter

# import re
# txt="The rain in Spain"
# x=re.split(r"\s",txt)
# print(x)

#we can control the number of occurences by specifying the masplit paremeter

#split the string only at the first occurences
# import re
# txt='The rain in Spain'
# x=re.split(r'\s',txt,2)
# print(x)



#the sub function
#the sub() function replaces the matches with the text of you choice

#replace every white space character with the number 9

# import re
# txt='The rain in Spain'
# x=re.sub("rain","9",txt) #replace the string with the character
# print(x)


#we can control the number of replacements by spacifying the count parameter

# import re
# txt='The rain in Spain'
# x=re.sub(r"\s","9",txt,1) #it give the one space replace the 9
# print(x)



#match objects
#A match object is an object containing information about the search and the result
import re
txt="The rain in spain"
x=re.search('ai',txt)
print(x) #this will print an object

#the mathc object has a properties and method used to retrieve information about the search and the result
#.span() return a tuple containing the start and end positions of the match
#.string() return the string passed into function
#.group()return the part of the string where there was a match

#the regular expression looks for any words that starts with an upper case "S"
import re
txt="The rain in Spain"
x=re.search(r"\bS\w+",txt)
print(x.span())

