#f string was introduced in python 3.6 and is now the preferred way of formatting strings
#f-string allows you to format selected parts of a string
#to specify a string as an f-string put an f in front of the string literal

#create the f strings
# txt=f'the price is 49 dollars'
# print(txt)


#placeholders and modifiers
#to format values in f string add placeholders a placeholder can contain variables, operations, functions and modifiers to format the value

#add a placeholder for the price variable
# price=59
# txt=f"the price is {price} dollars"
# print(txt)



#a placeholder can also include a modifier to format the value
#a modifier is included by adding a colon followed by legal formatting type

#display the price with 2 decimals

# price=59
# txt=f"the price is {price:.3f} dollars" #this give the 3 dot
# print(txt)

#we can also format a value directly without keeping it in a variable

# txt=f"the price is {95:.2f}dollars"
# print(txt)


#perform the operation of f strings
#we can perform python operation inside the placeholders
#we can do math operations

#perform a math operations in the placeholder and return the result
# txt=f"the price is {20*59} dollars"
# print(txt)


#we can perform math opeation on the variables
#add taxes before displaying the price

price=59
tax=0.25
txt=f"the price is {price+(price*tax)}"
print(txt)