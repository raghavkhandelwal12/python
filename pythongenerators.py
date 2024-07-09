#a generators in python is function that return an iterator using the yield keyword.

#geneartor function in python

#a generator function in python is defined like a normal function,but whenever it needs to generate a value.It does so with the yield keyword rather than return.


#create a generator in python
#in python we can create a generator function by simply using the def keyword and yield keyword.

# def function_name():
#     yield statement


#in this example we will create a simple generator that will yield three integer

#a generator function that yield  1 for the first time
#2 second time and 3 third time

# def simpleGeneratorFunc():
#     yield 1
#     yield 2
#     yield 3
    
    
# #driver code to check above generator function

# for value in  simpleGeneratorFunc():
#     print(value)



#Generator object
#python generator function return a generator object that is iterable i.e can be used as an iterator

#a python program to demonstrate use of
#generate object with next()

# def simpleGeneratorFunc():
#     yield 'abcd'
#     yield [2,3,4,5,6]
#     yield 3
    
# # #x is generator object
# x=simpleGeneratorFunc()

# #iterator over the generator object using next
# #in python3 ,__next__()

# print(next(x))
# print(next(x))
# print(next(x))



#in this example create two generator for fibonacci number first a simple generator and second generator using a for loop

#a simple generator for fibonacci numbers
# def fib(limit):
    
#     #Initialize first two fibonacci numbers
#     a,b=0,1
    
#     #one by one yield next fibonacci number
#     while a<limit:
#         yield a
#         a,b=b,a+b
# #create a generator object
# x=fib(5)

# #iterator over the generator object using next
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x)) 

# #iterating over the generator  object using for 
# print("\n using for in loop")
# for i in fib(5):
#     print(i)



#python generator expression
#in python generator expression is another way of writing the generator function.It uses the python list  comprehension technique.


#generator expression syntax

# (expression for item in iterable)


#generator expression
generator_exp=(i*5 for i in range(5) if i%2==0)
for i in generator_exp:
    print(i)