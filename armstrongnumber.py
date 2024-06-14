#function to check the armstrong numbers 
def is_numbers(num):
    #convert number to string to iterate over digits
    
    digits=[int(d)for d in str(num)]
    #calculate the sum of each digit to the power of the number of digit
    num_digits=len(digits)
    armstrong_sum=sum(pow(d,num_digits)for d in digits)
    #check if the sum is equal to the origional number
    return num==armstrong_sum

    #input 
user_input=input('enter four numbers separeated by spaces')
#split the input the strings into a list of string then convert each to an integer
numbers=[int(num)for num in user_input.split()]
#ensure exactly four numbers are entered
if len(numbers)!=4:
    print('please enter exactly four numbers')
else:
    armstrong_numbers=[num for num in numbers if is_numbers(num)]
    print('armstrong numbers',armstrong_numbers)
