#what is dataframe
#a pandas dataframe is 2 dimensional data structure like 2 dimesional array,or a table with rows and colu,ns


#create a pandas dataframe

# import pandas as pd
# data={
#     'calories':[420,454,333],
#     'duration':[50,40,45]
# }
# df=pd.DataFrame(data)
# print(df)


#local row
#we can see the result above the dataframe is like a table with rows and columns

#pandas use the loc attribute to return one or more specified row

# import pandas as pd
# data={
#     'calories':[420,454,333],
#     'duration':[50,40,45]
# }
# df=pd.DataFrame(data)
# print(df.loc[0])
# print(df.loc[[0,1]])


#when using [], the result is a pandas dataframe

#Named index
#with the index argument we can name our own indexed

#Add a list of names to give each row a name
# import pandas as pd
# data={
#     'calaories':[345,456,333],
#     'duration':[50,40,35]
# }
# df= pd.DataFrame(data,index=['day1','day2','day3'])
# print(df)


#locate named indexes
#use the names index in the loc attribute to return the specified row(s)
#return the day2
import pandas as pd
data={
    'calaories':[345,456,333],
    'duration':[50,40,35]
}
df= pd.DataFrame(data,index=['day1','day2','day3'])
print(df.loc['day2'])