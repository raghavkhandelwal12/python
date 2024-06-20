quote = ("Brave Sir Robin ran away. Bravely ran away away. When danger reared it's ugly head, "
         "he bravely turned his tail and fled. Brave Sir Robin turned about and gallantly he "
         "chickened out...")
a={}
for b in quote:
    if b in a:
        a[b]+=1
    else:
        a[b]=1
    
print(a)




