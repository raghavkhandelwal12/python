#the word polymorphism means many forms and in programming it refer to method fucntion operators with the same name that can be executed on many objects or classes
#function polymorphism
#an example of a python functions that can be used on different object is the len function

#class polymorphism
#polymorphism is often used in class  methods where we can have muliple classes with the same method name

#different classes with the same method

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print('Drive!')

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print('sail!')

class Plane:
    def __intit(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print('fly')
        
car1=Car('ford','mustang')
boat1=Boat('ibiza','touring20')
plane1=Plane('boeing','743')

for x in (car1,boat1,plane1):
    x.move()
        
        