#list add items
#append items
#to add an items to the end of the list use the append method

# thislist=['apple','banana','cherry']
# thislist.append('orange') #add the oragne at the ending of hte list
# print(thislist)


#extend the list
#to append elements from another list to the current list use the extend methdo
#add the elemetns of tropical to thislist

# thislist=['apple','banana','cherry','kiwi']
# tropical=['mango','cherry','papaya']
# thislist.extend(tropical)
# print(thislist)


#the extend() method does not have to append the list items
#add any iterable
# thislist=['apple','papaya','banana']
# tropical=('cherry','orange')
# thislist.extend(tropical)
# print(thislist)


#remove the list items
#the remove method remove the specified items

# thislist=['apple','banana','cherry']
# thislist.remove('banana')
# print(thislist)

#if there are more than one items with the specified value the remove method removes the first occurence

# thislist=['apple','banana','cherry','banana']
# thislist.remove('banana')
# print(thislist)


#remove the specified the index
#the pop() method remove the specified the index
# thislist=['apple','banana','cherry']
# thislist.pop(1)
# print(thislist) #this method remove the first index items


#if we not give the index number it remove the last items of the list
# thislist=['apple','banana','cherry']
# thislist.pop()
# print(thislist)


#the del keyword
# thislist=['apple','banana','cherry']
# del thislist[0]
# print(thislist)


#delete the entire list
# thislist=['apple','banana','cherrry']
# del thislist


#clear the list
# thislist=['apple','banana','cherry']
# thislist.clear()
# print(thislist) #this method not give the error if we clear the list


#loop list
#you can loop through the list items by using a for loop

# thislist=['apple','banana','cherry']
# for x in thislist:
#     print(x)


#looping through the index number
#you can also loop through the list items by referring to their index number
#use the range() and len() function to create a suitable iterable

# thislist=['apple','banana','cherry']
# for i in range(len(thislist)):
#     print(thislist[i])

#using a while loop
#you can loop through the list items by using the while loop
# thislist=['apple','banana','cherry']
# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i=i+1
    
    
#Looping using list comprehension
# thislist=['apple','banana','cherry']
# [print(x) for x in thislist]


#list comprehension
#list comprehension offers a shorter syntax when you want to create a new list baesd on the values of an existing of an extisting list

# fruits=['apple','banana','cherry','kiwi','mango']
# newlist=[]
# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)
# print(newlist)

# fruits=['apple','banana','cherry','kiwi']
# newlist=[x for x in fruits if 'a' in x]
# print(newlist)

#sort list
#list object have a sort()

# thislist=['apple','papaya','mango','watermelon','kiwi']
# thislist.sort()
# print(thislist)


#sort the list
# thislist=[100,54,5,66,33,22]
# thislist.sort()
# print(thislist)


#sort the list the descending order
# thislist=['orange','apple','cherry','kiwi','papaya']
# thislist.sort(reverse=True)
# print(thislist)


#customize sort function
# def myfunc(n):
#     return abs(n-50)

# thislist=[100,50,65,75,70]
# thislist.sort(key=myfunc)
# print(thislist)


#case sensitive
# thislist=['banana','Orange','Kiwi','cherry']
# thislist.sort()
# print(thislist)


#perform case sensitive sort of the list
# thislist=['banana','Orange','Kiwi','cherry']
# thislist.sort(key=str.lower)
# print(thislist)


#reverse order
#the reverse() method reverse the current sorting order of the elements
#reverse the order of the last items

# thislist=['banana','Orange','Kiwi','cherry']
# thislist.reverse()
# print(thislist)


#copy list

#make a copy of a list with the copy() method
# thislist=['apple','banana','cherry']
# mylist=thislist.copy()
# print(mylist)


#another way to make a copy is to use the built in the method

# thislist=['apple','banana','cherry']
# mylist=list(thislist)
# print(mylist)


#python join list
# list1=['a','b','c']
# list2=[1,2,3]
# list3=list1 + list2
# print(list3)

#append list into list1
# list1=['a','b','c']
# list2=[1,2,3]
# for x in list2:
#     list1.append(x)
# print(list1)


#use the extend() method to add list2 at the end of list1

list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2)
print(list1)