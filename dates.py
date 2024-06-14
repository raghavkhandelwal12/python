#a date in python is not data type its own but we can import a module name date time
#import the datetime module and display the current date

# import datetime
# x=datetime.datetime.now()
# print(x)

#return the year and named of weekday

# import datetime
# x=datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))


#creating date objects

# import datetime
# x=datetime.datetime(2024,3,17)
# print(x)

#the strftime() method

#the datetime objects has a method for fomratting date objects into readable strings

#this method is called strftime() and takes one parameter fromat to specify the format of the returrned strings

# import datetime
# x=datetime.datetime(2018,6,1)
# print(x.strftime("%B"))


# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%a"))

# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%A"))



# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%w"))


# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%d"))


#%b give the name of the month in the short name
# import datetime
# x=datetime.datetime.now()
# print(x.strftime('%b'))


#%B give the full name of hte month
# import datetime
# x=datetime.datetime.now()
# print(x.strftime('%B'))


#   %y give the short version of the year

# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%y"))


#%Y give the full version of the year
# import datetime
# x=datetime.datetime.now()
# print(x.strftime('%Y'))

# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%H,%M,%S"))

#%H 
# import datetime
# x=datetime.datetime.now()
# print(x.strftime('%H'))

# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%I"))


# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%p")) #this print the am and pm

# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%M")) #this M print the only Minute


# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%S")) #this print the second only

# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%f")) #tis print the micro second

# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%z"))


# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%j")) #this print the counting the day

# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%U")) #tis print the which week is continue


# import datetime
# x=datetime.datetime.now()
# print(x.strftime('%W'))


import datetime
x=datetime.datetime.now()
print(x.strftime("%c"))

