#inheritence allows us to define a class that inherits all the method  and properties of the another class
#parent class is the class being inherited from also called the base class
#child class is the class that inherits from the another class also called the derived class


#create a parent class
#any class can be parent class so the syntax is the same name as creating any other class

# class Person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# class Student(Person):
#     pass
# x=Student('raghav','khandelwal')
# x.printname()


#add the init  function
# class Person:
#     def __init__(self,fname ,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# class Student(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname)

# x=Student('raghav','k')

# x.printname()



#use the super function


#the super function

# class Person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# class Student(Person):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)

# x=Student('raghav','kg')
# x.printname()


#add propertires
# class Person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# class Student(Person):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)
#         self.graduationyear=2025
# x=Student('raghav','khandelwal')
# print(x.graduationyear)


# class Person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def printname(self):
#         print(self.fname,self.lname)
# class Student(Person):
#     def __init__(self,fname,lname,year):
#         super().__init__(fname,lname)
#         self.graduationyear=year
# x=Student('r','k',2025)
# print(x.graduationyear)


class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
        
    def welcome(self):
        print('welcome',self.fname,self.lname,"to the class of",self.graduationyear)
        
x=Student('raghav','khandelwal',2025)
x.welcome()