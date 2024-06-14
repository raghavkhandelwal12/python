#python program to find simple interest for given principle amount and  rate of interest

# def simple_interest(p,t,r):
#     print('the principle is' ,p)
#     print('the time period is',t)
#     print('the rate of interest is ',r)
#     si=(p*r*t)/100
#     print('the simple interest is',si)
#     return si

# simple_interest(8,6,8)


#principle amount,time and rate of interst taken form user

def simple_interest(p,t,r):
    print('the principle amount is ',p)
    print('the time period is ',t)
    print('the rate of interest is',r)
    
    si=(p*r*t)/100
    print('the simple interest is ',si)
    return si
P=int(input('enter the prinicple amount'))
T=int(input('enter the time period '))
R=int(input('enter the rate '))
simple_interest(P,T,R)
