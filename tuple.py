#tuple are used to store multiple items in a single variable
#a tuple is a collection which is ordered and unchangeable
#tuple are written in round brackets

# thistuple=('apple','banana','cherry')
# print(thistuple)

#tuple items are ordered ,unchangeable and allow duplicate values

# thistuple=('apple','banana','cherry','apple','cherry')
# print(thistuple)
# print(len(thistuple))


#create a tuple items into one items
# thistuple=('apple',)
# print(thistuple)
# print(type(thistuple))


#tuple constructor
# thistuple=tuple(('apple','banana','cherry'))
# print(thistuple)
# print(type(thistuple))


#access tuple items
# thistuple=('apple','banana','cherry')
# print(thistuple[1])


#negative indexing
# thistuple=('apple','banana','cherry')
# print(thistuple[-1])


#range of indexes
# thistuple=('apple','banana','cherry','kiwi','mango','papaya')
# print(thistuple[2:5])

# thistuple=('apple','banana','cherry','kiwi','orange','mango')
# print(thistuple[:4])


# thistuple=('apple','banana','cherry','kiwi','papaya')
#  print(thistuple[2:])
# print(thistuple[-4:-1])


#check if item exists

#to determine if a specified item is present in a tuple use the in keyword

# thistuple=('apple','banana','cherry')
# if 'apple' in thistuple:
#     print('yes, apple is present')


#python update tuple
#once a tuple is created you cannot change its values tuples are unchangeable or immutable as it also is called
# x=('apple','banana','cherry')
# y=list(x)
# y[1]='kiwi'
# x=tuple(y)
# print(x)


#convert the tuple into  a list add orange and conveert it back into a tuple

# thistuple=('apple','banana','cherry')
# y=list(thistuple)
# y.append('orange')
# thistuple=tuple(y)
# print(thistuple)


# thistuple=('apple','banana','cherry')
# y=('orange',)
# thistuple+=y
# print(thistuple)


#remove items
thistuple=('apple','banana','cherry')
y=list(thistuple)
y.remove('apple')
thistuple=tuple(y)
print(thistuple)