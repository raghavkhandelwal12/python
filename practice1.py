#add two number with + operator
# num1=15
# num2=34
# sum=num1+num2
# print(sum)


#add two number using the input function
# a=int(input('enter the first number'))
# b=int(input('enter the second number'))
# c=a+b
# print(c)

#add two number using the python function
# def add(a,b):
#     return a+b
# num1=10
# num2=15
# sum=add(num1,num2)
# print(sum)


#add two number to add two numbers
# num1=15
# num2=10
# import operator
# su=operator.add(num1,num2)
# print(su)

#add two number using the lambda function
# x=lambda a,b:a+b
# print(x(5,9))


#add two numbrt using the recursive function
# def add_numbers_recursive(x,y):
#     if y==0:
#         return x
#     else:
#         return add_numbers_recursive(x+1,y-1)
# #take the input to the user
# num1=9
# num2=3
# result=add_numbers_recursive(num1,num2)
# print(result)


#minimum of two numbers
#python program to find the minimum numbers of two numbers

# def minimum(a,b):
#     if a<=b:
#         return a
#     else:
#         return b
# a=2
# b=4
# print(minimum(a,b)) 


#python program to find out the minimum of two numbers
# a=2
# b=4
# minimum=min(a,b)
# print(minimum)


# a=2
# b=4
# print(sorted([a,b])[0])


#using the module to find out the minimum numbers
# from functools import reduce
# a=2
# b=4
# minimum=reduce(lambda x,y:x if x<y else y,[a,b])
# print(minimum)


#find maximum of two numbers in the python

# def maximum(a,b):
#     if a>=b:
#         return a
#     else:
#         return b
# a=2
# b=4
# print(maximum(a,b))



#find the maximum of two numbers using the max function
# a=2
# b=4
# maximum=max(a,b)
# print(maximum)



#find the maximum of two numbers using the ternary operator
# a=2
# b=4
# print(a if a>b else b)


#find out the maximum of two numbers using the lambda function

# a=2
# b=4
# maximum=lambda a,b:a if a>b else b
# print(f'{maximum (a,b)} is a  maximum number')

#maximum of two numbes using the list comprehension

# a=2
# b=4
# x=[a if a>b else b]
# print('the maximum number is',x)

#maximum of two numbers using the sort method
# a=2
# b=4
# x=[a,b]
# x.sort()
# print(x[-1])


#python program to find the gcd of two numbers

#Python code to demonstrate the working of gcd()
# import math
# print('the gcd of 60  and 48 is :',end="")
# print(math.gcd(60,48))


#python program to find the gcd of two numbers using the recursion
# def hcf(a,b):
#     if(b==0):
#         return a
#     else:
#         return hcf(b,a%b)
# a=60
# b=48
# print('the gcd of 60 and 48 is ', end="")
# print(hcf(60,48))


#python program to add the two binary numbers
a='1101'
b='100'
max_len=max(len(a),len(b))
a=a.zfill(max_len)
b=b.zfill(max_len)
