#find the size of a tuple in a python
#the getsizeof() function belongs to the python sys module.It has been implemented in the below

# import sys
# tuple1=('A','B',2,'C',3)
# tuple2=('raghav','abc')
# print('size of tuple1: '+str(sys.getsizeof(tuple1)))
# print('size of tuple2: '+str(sys.getsizeof(tuple2)))



#python program to create a list of tuples from given list having number and its cube in each tuple

#creating a list
# list=[1,2,5,6]
# using the list comprehension to iterate each
# values in list and create a tuple as specified
# res=[(val,pow(val,3))for val in list]
# print(res)


#using the **opearotr
# list=[1,2,5,6]
# res=[(val,val**3)for val in list]
# print(res)



#using the map and lamda function
# list1=[1,2,5,6]
# res=list(map(lambda x:(x,x**3),list1)) #the map function will apply this lambda function to lall element of the list and return a list of tuple
# print(res)


#adding tuple to list and vice versa
#intialize the list
# l1=[5,6,7]
# printing origional list
# print(l1)

#initialize the tuple
# tup=(9,10)
# l1+=tup
# print(l1)


#python flatter tuple of list to tuple

#using the sum() +tuple()we can perform the task of the flattening using sum(),passing an empty list as its argumetns

#flatten tuple fo list to tuple using sum() + tuple()

#intialize tuple
# t=([5,6],[6,7,8,9],[3])
#printing the origional tuple
# print('the origional tuple:'+str(t))
#flatten tuple of list to tuple 
#using the sum()+tuple()
# res=tuple(sum(t,[]))
# print(res)



#python convert nested tuple to custom key dictionary
#using the list comprehension +dictionary comprehension
#initialize tuple
# t=((4,'abc',10),(3,'is',8),(6,'best',10))
# print(str(t))

# convert nested tuple to custom key dictionary
# res=[{'key':sub[0],'value':sub[1],'id':sub[2]}for sub in t]
# print(str(res))


#flatten tuple of list to tuple

# t=([2,3],[5,6,7,8],[3])
# print(t)
# tes=tuple(sum(t,[]))
# print(tes) #this give the result in the form of the tuple


#python order tuple by list

