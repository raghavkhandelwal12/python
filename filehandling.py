#file handling is an important part of any web application
#python has a several functions for creating,reading,updating and delting files

#the key function for working with files in python is the open() function
#the open() function take two parameters filename and mode
#there are four different methods for opening a file

#'r' read default value opens a file for reading error if the file does not exist
#'a' append opens a file for appending created the file if it does not exist
#w -write open a files for writing ,creates the file if it does not exist
#x create create the specified file return an error if the file exist
#'t' test default value.text mode
#'b' bindary mode

# f=open("demofile.txt")
# f=open('demofile.txt','r')

#to open the file use the built in open() function
#the open() function return a file object which has a read() method for reading the content of the file

# f=open('demofile.txt','r')
# print(f.read()) #this print thhe demofile.txt content

#reads only parts of the file
#by default the read() method return the whole text but we can also specify how many characters we want to return


#to return the 5 first charcters of the file
# f=open('demofile.txt','r')
# print(f.read(5))



#read lines 
#we can return one line by using the readline() method
#read one line of the file

# f=open('demofile.txt','r')
# print(f.readline()) #this print the only one line


#by looping through the lines of the file we can read the whole file line by line
#looping through the file line by line

# f=open('demofile.txt','r',)
# for x in f:
#     print(x)


#if a good practice to always close the file when you are done with it

# f=open('demofile.txt','r')
# print(f.readline())
# f.close()


#python file write
#to write to an existing file you must to add a parameter to the open function()

#'a' -append will append to the end of the file
#'w'-write will overwrite any existing content

# f=open('demofile2.txt','a')
# f.write('hi you are very intelligent')
# f.close()

# #open and read the file after the appending
# f=open('demofile2.txt','r')
# print(f.read())


#open the file  and overwrite the content
# f=open('demofile2.txt','w')
# f.write('hello the computer science is very nice subject')
# f.close()

#open and read the file after the overwriting
# f=open('demofile2.txt','r')
# print(f.read())


#create a new file in python use the python metho with one of the following parameter

#x-create will create a file return an error if the file exist

# f=open('myfile.txt','x') #the x create the new file

#to delete a file you must import the os module and run its os.remove() function

# import os
# os.remove('demofile.txt')#this remove the demofile.txt in the file

#check if the file exist or not 
#to avoid getting an error you might want to check if the file exist befor you try to delete it

import os
if os.path.exists('demofile.txt'):
    os.remove('demofile.txt')
else:
    print('the file does not exist')
