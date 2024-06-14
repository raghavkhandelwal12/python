#variable that are created outside of a function are known as a global variables
#global variable can be used everyone both inside and outside the function

# x='awesome'
# def myfunc():
#     x='fantastic'
#     print('pyton is ' +x)
# myfunc()


#create a variable inside a function with the same name as the global variable

# x='awesome'
# def myfunc():
#     x='fantastic'
#     print('python is ' +x)
# myfunc()
# print('python is '  +x)


#the global keyword
#to create global variable inseide a function you cna use the global keyword

# def myfunc():
#     global x
#     x='fantastic'
# myfunc()
# print('python is ' +x)


#to change the value of the global variable inside a function refer to the variable by using the global keyword
x='awesome'
def myfunc():
    global x
    x='fantastic'
myfunc()
print('python is ' +x)