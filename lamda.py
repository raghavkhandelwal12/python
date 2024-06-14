#a lamda function is a small anonymous function
#a lamda function can take any number of arguments but can only have one expression

#add a 10 to argument
# x=lambda a:a+10
# print(x(6))


#lamda function can take any number of argument
#multiply argument a with argument b and return the rsult
# x=lambda a,b:a*b
# print(x(4,5))


#summarize argument a,b,c and return the result
# x=lambda a,b ,c:a+b+c
# print(x(3,4,5))


#why use the lambda function
# def myfunc(n):
#     return lambda a:a*n

# mydoubler=myfunc(2)
# print(mydoubler(11))


# def myfunc(n):
#     return lambda a:a*n

# mytripler=myfunc(3)
# print(mytripler(11))

#or use the same function definition to make both function,in the same program

def myfunc(n):
    return lambda a:a*n

mydoubler=myfunc(2)
mytripler=myfunc(3)
print(mydoubler(11))
print(mytripler(22))



