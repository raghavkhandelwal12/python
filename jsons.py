#json in a syntax for storing and exchanging data
#json is text writtern with javascript object notation

#python has a built in package called json which can be used to work with json data
# import json
# #parse json  convert from json to python
# x='{"name":"raghav" , "age":30,"city":"New york"}'

# y=json.loads(x)
# print(y['age'])
# print(x)


#convert python to json
import json
x={
    "name":"john",
    "age":30,
    "city":"New york"
    }
#convert into the json
y=json.dumps(x)
print(y)
