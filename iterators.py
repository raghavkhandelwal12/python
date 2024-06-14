#an iterator is an object that contains a countable numbers of values
#list tuple and dictionaries and sets are all iterable objects,they are iterable containers which you can get an iterator form
#return an iterator from a tuple and print each value

# mytuple=('apple','banana','cherry')
# myit=iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))


#even strings are iterable objects and can return an iterator
#strings are also iterable objects containing a sequence of character

# mystr='banana'
# myit=iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

#looping through the iterator
# mytuple=('apple','banana','cherry')
# for x in mytuple:
#     print(x)

#iterate the character of a strings
# mystr='banana'
# for x in mystr:
#     print(x)


#create an iterator
#to create an object/class as an iterative you have to implement the method __iter__() and __next__() to your object

# class MyNumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
# myclass=MyNumbers()
# myiter=iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


#stopiteration
#to stop the iteration we use the stopiteration

class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if slef.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=MyNumbers()
myiter=iter(myclass)

for x in myiter:
    print(x)
  
    