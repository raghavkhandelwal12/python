#what is series
#a pandas series is like a column in a table
#It is one dimensional array holding data of any type

#create a simple pandas series from a list
# import pandas as pd
# a=[1,7,2]
# myvar=pd.Series(a)
# print(myvar)

#labels 
#if nothing else is specified the values are labelled are labeled with their index number.
#the label is used to access a specific value

# print(myvar[0])



#create labels
#with the index argument we can name your own labels
# import pandas as pd
# a=[1,7,2]
# myvar=pd.Series(a,index=['x','y','z'])
# print(myvar['y'])
# print(myvar)


#key/value objects as series
#we can also use a key/values object like a dictionary,when creating a series

#create a simple pandas series from a dictionary

# import pandas as pd
# calories={'day1':420,'day2':380,'day3':390}
# myvar=pd.Series(calories)
# print(myvar)


#the key of the dictionay becomes the labels

#to select only some of the items in the dictionary use the index argument and specify only the items you want to include the series

#create a series using data from day1 and day2

# import pandas as  pd
# myvar={'day1':420,'day2':454,'day3':444}
# m=pd.Series(myvar,index=['day1','day2'])
# print(m)


#Dataframe

#create a dataframe from two series
import pandas as pd
data ={
    'calaories':[420,380,390],
    'duration':[50,40,45]
}
myvar=pd.DataFrame(data)
print(myvar)
