#python program to interchange first and last elements in a list

def swap(newlist):
    size=len(newlist)
    
    #swapping
    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp
    return newlist

newlist=[12,35,9,56,24]
print(swap(newlist))