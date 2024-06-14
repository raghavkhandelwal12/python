#python program to find out the sum of array
# def _sum(arr):
#     sum=0
#     for i in arr:
#         sum=sum+i
#     return sum

# #main in function

# #input value to list
# arr=[14,3,4,15]
#     #calculating the length of the array
# n=len(arr)
# ans=_sum(arr)
# print(ans)


#python array sum using the sum function
# arr=[34,32,2,4,6]
# a=sum(arr)
# print(anext)


#python program to find out the sum of array using the reduce method
from functools import reduce
def _sum(arr):
    sum=reduce(lambda a,b:a+b,arr)
    return (sum)

arr=[44,55,33,22]
n=len(arr)
a=_sum(arr)
print(a)    