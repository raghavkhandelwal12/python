#python is an object oriented programming language
#a class is like an object construcotr or a blue print for creating a object

#create a class
# class MyClass:
#     x=5
# #to create an object named p1 and print the value of x
# p1=MyClass()
# print(p1.x)


#the init function

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=Person('raghav',21)
# print(p1.name)
# print(p1.age)

#the str function
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name}{self.age}"
# p1=Person('raghav',21)
# print(p1)


#object method
#object can also contain methods

#Let us create a metod in the person class

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print('hello my name is' + self.name)
# p1=Person('raghav',21)
# p1.myfunc()


#the self parameter

class Person:
    def __init__(abc,name,age):
        abc.name=name
        abc.age=age
    def myfunc(xyz):
        print('hello my name is ' + xyz.name)
p1=Person('raghav',21)
p1.age=20
del p1.age
print(p1.age)

p1.myfunc()

        