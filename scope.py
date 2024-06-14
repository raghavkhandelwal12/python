#local scope
#a variable created inside a function belongs to the local scope of that function a and can only be used inside that function

#a variable created inside  a function is available inside that function
# def myfunc():
#     x=300
#     print(x)
# myfunc()


#function inside function
#the local variable can be accessed from a function within the function
# def myfunc():
#     x=300
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()
# myfunc()


#a variable created outside of a function is global and be used by anyone
# x=300
# def myfunc():
#     print(x)
# myfunc()
# print(x)


#naming variable
#the function will print the local x, and then the code will print the global x

# x=300
# def myfunc():
#     x=200
#     print(x)
# myfunc()
# print(x)


#global keyword

#the global keyword make the variable global

# def myfunc():
#     global x
#     x=300
# myfunc()
# print(x)


#example of global keyword
# x=300
# def myfunc():
#     global x
#     x=200
# myfunc()
# print(x)

#nonlocal keyword
#the non local keyword is used to work with variable inside nested functions
#the nonlocla keyword makes the variables belongs to the outer function

#if you use teh nonlocal keyword the variable belongs to the outer function

def myfunc1():
    x='jane'
    def myfunc2():
        nonlocal x
        x='hello'
    myfunc2()
    return x
print(myfunc1())