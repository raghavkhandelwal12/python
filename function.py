#a function is a block of code which only runs when it is called
#you can pass data,known as parameter into a function
#a function can return data as result

#creating a function is define using the def keyword
# def myfunc():
#     print('hello from a function')
# myfunc() #to call a function use the function name followed by parenthesis

#arguments
#information can be passed into function as arguments
#argument are specified after the function name inside the parenthesis.we can add many arguments as you want

# def myfunc(fname):
#     print(fname + 'refsnes')
# myfunc('email')
# myfunc('tobias')
# myfunc('linus')


#paremeters or arguments
#a parameter is the variable listed inside the parenthesis in the function definition
#an argument is the value that is sent to the function when it is called



#the function expects 2 arguments and gets 2 arguments
# def myfunc(fname,lname):
#     print(fname + " " + lname)
# myfunc('email','refsnes')



#arbitary arguments
# def myfunc(*kids):
#     print('the youngest child is ' + kids[0])
# myfunc('email','tobias','linus')
 
 
 #keyword arguments
 #we can send arguments with the key =value syntax
 #this way the order of the arguments does not matter
 
# def myfunc(child3,child2,child1):
#     print('the youngest child is ' + child3)
    
# myfunc(child1='emil',child2='xyz',child3='mba')
    
    
    
#arbitary keyword arguments **kwargs
#if the number of keyword arguments is unknown add a double ** before the parameter name

# def myfunc(**kids):
#     print('his last name is ' + kids['lname'])
# myfunc(fname='raghav',lname='khandelwal')
     


#default parameter value
#if we call the function without arguments,it uses the default value

# def myfunc(country='india'):
#     print('i am from ' + country)
    
# myfunc('swedan')
# myfunc('china')
# myfunc()
# myfunc('brazil')


#passing a list an arguments

# def myfunc(food):
#     for x in food:
#         print(x)
# fruits=['apple','banana','cherry']
# myfunc(fruits)

#return a value
#to let a function return a value use the return statement

# def myfunc(x):
#     return 5*x
# print(myfunc(3))
# print(myfunc(5))
# print(myfunc(9))


#the pass statements

#function definition cannot be empty  put in the pass statement to avoid geeting an error
# def myfunc():
#     pass



#positional only arguments
#you can specify that a function can only positional argument or only arguments

#to specify that a function can have only positonal arguments add , / after the arguments
# def myfunc(x,/):
#     print(x)
# myfunc(3)

# def myfunc(x):
#     print(x)
# myfunc(x=3)


#it give the error
# def myfunc(x,/):
#     print(x)
# myfunc(x=3) #it give the erro


#keyword only arguments
#to specify that a function can have only keyword argumetns *before the argument
# def myfunc(*,x):
#     print(x)
# myfunc(x=3)


# def myfunc(x):
#     print(x)
# myfunc(3)


# def myfunc(*,x):
#     print(x)
# myfunc(3)



#combine postional only and keyword only
#you can combine the two arguments types in the same function

def myfunc(a,b,/,*,c,d):
    print(a+b+c+d)
myfunc(5,6,c=6,d=8)