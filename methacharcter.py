#metacharacter are characters with a special meaning
#[]this give the set of characer
# import re
# txt='the rain in spain'
# x=re.findall("[a-z]",txt) #this give the set of charcter iin the patterns
# print(x)


#\"d "this find out the all digit character


# import re
# txt='that will be 59 dollars'
# x=re.findall(r"\d",txt)
# print(x)

# import re
# txt='hello planet'
# x=re.findall('pl...t',txt) #the dot(.) give the word wise element
# print(x)



#^this tell the word start with 
# import re
# txt="hello planet"
# check if string starts with hello
# x=re.findall("^hello",txt)
# if x:
#     print('yes,the string start with hello')
# else:
#     print('no string start not the hello')


#$ this symbol tell the string end the word which we mention in the txt
# import re
# txt='hello planet'
# #check if the string end the planet
# x=re.findall("planet$",txt)
# if x:
#     print('string end the planet')
# else:
#     print('np')


# *zero or more occurence
# import re
# txt="helertylo planet"
# #search for a sequence that starts with 'he' followed by 0 or more characeter and an "o"
# x=re.findall("he.*o",txt)
# print(x)

#to print the one or more occurence
# import re
# txt='ragahv my name is raghav'
# x=re.findall("ra.+name",txt) #this tell the word which i mention in the code go to the this word
# print(x)


#?zero or one occurence
# import re
# txt='heo planet'
# #searches for a sequence that starts with "he" followed by 0,1 characer and an o

# x=re.findall("h.?o",txt) #this print the complete heo 
# print(x)



# import re
# txt='hhjkeertee toy boy'
# x=re.findall('hh.?e',txt)
# print(x)


#{}exactly the specified number of occurence
# import re
# txt='hello planet'
# x=re.findall('he.{2}o',txt)
# print(x)



#either or | falls|stays
import re
txt='the rain in spain falls mainly in the plain'

x=re.findall('falls|stays',txt)
print(x)
if x:
    print('yes at least one mathc')
else:
    print('no match')