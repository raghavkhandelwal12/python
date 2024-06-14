#python program to find  compound interest using the python
# def compound_interest(p,r,t):
#     #calculate the compound interest
#     Amount=p*(pow((1+r/100),t))
#     CI=Amount-p
#     print('compound interest',CI)
# compound_interest(10000,10.25,5)


#calculate the compound interest using the taking the input
# def compound_interest(p,t,r):
#     amount=p*(pow((1+r/100),t))
#     ci=amount-p
#     print('the compound interest is',ci)
    
# p=int(input('enter the principle'))
# r=int(input('enter the rate'))
# t=int(input('enter the time'))
# compound_interest(p,r,t)


#to find out the compoud interest
p=1200
r=2
t=5.4
a=p*(pow((1+r/100),t))
ci=a-p
print(ci)

